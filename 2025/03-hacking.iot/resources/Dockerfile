# Použitie oficiálneho Kali Linux image
FROM kalilinux/kali-last-release:latest

# Aktualizácia balíčkov a inštalácia
# tools selection: https://www.kali.org/tools/
RUN apt-get update && apt-get install --no-install-recommends --yes \
        bettercap=2.33.0-1kali1 \
        iputils-ping=3:20240905-1 \
        john=1.9.0-Jumbo-1+git20211102-0kali9 \
        netcat-traditional=1.10-50 \
        nmap=7.95+dfsg-1kali1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Nastavenie pracovného adresára
#WORKDIR /root

# Štandardný príkaz na spustenie Bash shellu
# CMD [ "/bin/bash" ]
