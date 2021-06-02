## Inštalácia _Minetest_-u v _OS Linux_

1. Z balíčkovacieho sytému distribúcie si nainštalujte balík `minetest`:

    ```bash
    # ak pouzivate Debian/Ubuntu/Mint
    $ sudo apt install minetest

    # ak pouzivate RedHat/Fedoru
    $ sudo dnf install minetest
    ```

2. Spustite a vypnite `minetest`, čím sa vo vašom domovskom priečinku vytvorí priečinok `~/.minetest/` a v ňom súbor s konfiguráciou `minetest.conf`. Zapíšte do neho riadok:

    ```
    secure.enable_security = false
    ```

3. V priečinku `~/.minetest/` vytvorte priečinok `mods/`. Stiahnite a rozbaľte do neho posledné vydanie _0.20_ projektu [raspberryjammod-minetest](https://github.com/arpruss/raspberryjammod-minetest):

    ```bash
    $ cd ~/.minetest
    $ mkdir mods/ && cd mods/
    $ wget https://github.com/arpruss/raspberryjammod-minetest/releases/download/0.20/raspberryjammod-minetest-windows-msvc.zip
    $ unzip raspberryjammod-minetest-windows-msvc.zip
    $ rm raspberryjammod-minetest-windows-msvc.zip
    ```


3. Do distribúcie si doinštalujte balík `lua5.1-socket`:

    ```bash
    # ak pouzivate RedHat/Fedora
    $ sudo dnf install lua5.1-socket
    ```


## Inštalácia _Minetest_-u v _OS Windows_


## Vytvorenie sveta


