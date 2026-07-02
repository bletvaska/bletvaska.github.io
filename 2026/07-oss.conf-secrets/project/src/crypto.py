import os
import binascii
import machine
import hashlib
import cryptolib


SALT_FILE = '/data/.salt'

def create_salt(salt_path: str = SALT_FILE) -> None:
    with open(salt_path, 'wb') as file:
        file.write(os.urandom(16))

def create_key(salt_path: str = SALT_FILE) -> bytes:
    with open(salt_path, 'rb') as file:
        salt = file.read()

    hasher = hashlib.sha256()

    # adding data to hash
    hasher.update(machine.unique_id())
    hasher.update(salt)

    # return hash
    return hasher.digest()[:16]  # AES-128


def encrypt(plaintext: str, salt_path: str = SALT_FILE) -> str | None:
    if plaintext is None:
        return None

    key = create_key(salt_path)
    iv = os.urandom(16)
    data = plaintext.encode('utf-8')
    pad = 16 - (len(data) % 16)
    data = bytearray(data + bytes([pad] * pad))
    cipher = cryptolib.aes(key, 2, iv)
    encrypted = cipher.encrypt(data)

    return binascii.hexlify(
        bytearray(iv) + bytearray(encrypted)
    ).decode('ascii')


def decrypt(ciphertext: str, salt_path: str = SALT_FILE) -> str | None:
    if ciphertext is None:
        return None

    key = create_key(salt_path)
    raw = binascii.unhexlify(ciphertext)
    iv = raw[:16]
    data = bytearray(raw[16:])
    cipher = cryptolib.aes(key, 2, iv)
    decrypted = cipher.decrypt(data)
    pad = decrypted[-1]
    return bytes(decrypted[:-pad]).decode('utf-8')