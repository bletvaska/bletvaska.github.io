# Notes

## Instalacia node-u

`node-red-node-sqlite`


## Vytvorenie DB

* flow: `Inject` > `SQLite`
* pridat umiestnenie novej db: `/tmp/db.sqlite`
* pridat fix code:

    ```sql
    CREATE TABLE light(
        TIMESTAMP INT PRIMARY KEY NOT NULL,
        VALUE INT NOT NULL
    );
    ```

## Kontrola cez `sqlite3`

* z prikazoveho riadku:

    ```bash
    $ sqlite3 /tmp/db.sqlite
    ```

* pozriet sa na zoznam tabuliek a schemu:

    ```bash
    .tables
    .schema light
    ```


## `INSERT` do db

* pridat function uzol do flow-u, ktory zacina MQTT: `MQTT In` > `save light` > `SQL Query`

* do kodu funkcie pridame SQL kod, ktory odide cez `msg` objekt cez `.topic`:

    ```javascript
    msg.topic = `INSERT INTO light VALUES(
        "${flow.get('timestamp')}",
        "${flow.get('light')}"
    )`;

    return msg;
    ```


## Rozsirenie www stranky

* do www stranky pridame zoznam poslednych 10 merani ako tabulku

* pridame SQLite uzol medzi `HTTP In` a `Template`

* vlozime fixed query do noveho SQLite uzla:

    ```sql
    SELECT *
    FROM light
    ORDER BY timestamp DESC
    LIMIT 10;
    ```

* do sablony pridame:

    ```html
    <h2>Historické údaje</h2>

    <table border="1">
        <tr>
            <th>cas</th><th>data</th>
        </tr>
        {{#payload.length}}
        {{#payload}}
        <tr>
            <td>{{TIMESTAMP}}</td>
            <td>{{VALUE}}</td>
        </tr>
        {{/payload}}
        {{/payload.length}}
    </table>
    ```


## Template v UI

* pridame uzol `Template` pre UI

* zaradime na koniec flow-u, kde data zbierame z `MQTT In`: `SQLite` > `UI Template`

* do `SQLite` pridame fix query:

    ```sql
    SELECT *
    FROM light
    ORDER BY timestamp DESC
    LIMIT 10;
    ```
* do sablony vlozime nasledovny kod:

    ```html
    <table style="width:100%">
      <tr>
        <th>Timestamp</th>
        <th>Value</th>
      </tr>

      <tr ng-repeat="x in msg.payload">
        <td>{{msg.payload[$index].TIMESTAMP}}</td>
        <td>{{msg.payload[$index].VALUE}}</td>
      </tr>
    </table>
    ```
