try:
    import usocket as socket
except:
    import socket
try:
    import ustruct as struct
except:
    import struct

# (date(1970, 1, 1) - date(1900, 1, 1)).days * 24*60*60
NTP_DELTA = 2208988800

# The NTP host can be configured at runtime by doing: ntptime.host = 'myhost.org'
host = "pool.ntp.org"


def time():
    query = b'\x1b' + 47 * b'\0'
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    res = s.sendto(query, addr)
    data = s.recv(48)
    s.close()
    t = struct.unpack('!12I', data)[10]
    return t - NTP_DELTA


def settime():
    t = time()
    from machine import RTC
    from utime import gmtime
    
    tm = gmtime(t)
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    RTC().datetime(tm)
