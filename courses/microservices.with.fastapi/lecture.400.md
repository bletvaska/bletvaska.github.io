---
title: Health Check API
courseid: fastapi
order: 400
layout: lecture
description: |
    kontrola stavu mikrosluzby
---

![Health Check](images/health.check.jpg)

## TODO

* pre FastAPI je na to modul https://github.com/Kludex/fastapi-health


## Problem

* spravovať distribuované systémy je náročné. skladajú sa totiž z veľkého množstva súčastí, ktoré potrebujú pracovať (a spolupracovať), aby systém mohol ako celok fungovať.

* ak sa niektorá jeho súčať pokazí, systém ju musí:

    * detegovať, napr. vytvorením alertu, 
    * obísť ju, napr. load balancer nebude posielať požiadavky na nefungujúcu službu, a 
    * opraviť ju, resp. zotaviť sa z nej. 

* a to všetko sa musí udiať automagicky.

* ako teda detegovať, že bežiaca služba nedokáže spracovávať požiadavky?


## Health Check

### Overview

* **health check** poskytuje jednoduchý mechanizmus, pomocou ktorého je možné overiť, či daná služba pracuje správne. obyčajne má služba vytvorené **Health Check API** pomocou protokolu HTTP (napr. `/health`), ktorá pomocou stavových kódov hovorí o stave služby. Je možné sa však stretnúť aj s prípadmi, kedy sa kontrola stavu služby vykonáva pomocou metódy `HEAD` nad niektorým existujúcim endpointom.

* okrem stavového kódu sa môže vo výsledku HTTP požiadavky nachádzať aj krátky JSON dokument, ako napr.:

  ```json
  {
      "status" : "UP" 
  }
  ```

* v rámci kontroly zdravia služby sa môže overovať napr.:

    * stav spojenia s ostatnými službami,
    * stav stroja, napr. jeho diskový priestor, využitie pamäte a pod.,
    * špecifická logika aplikácie,
    * stav databázy,
    * a iné.


### Health Check in Containers

* okrem toho však s kontrolou stavu súvisí aj kontrola stavu kontajnera, v ktorom je aplikácia spustená. kontajnery totiž bežia 24/7 a aj tu môže dôjsť k niektorým situáciám:

    * stav kontajneru
    * aktualizácia aplikácie v kontajneri

* takže ak aplikácia beží v kontajneri a ten je spustený, nemusí to hneď znamenať, že aplikácia vo vnútri kontajneru parcuje správne. kontrolu teda treba vykonávať ako na úrovni aplikácie, tak aj na úrovni kontajnera.


### Health Check in Virtual Machines

* Tento prístup však nie je vhodný, ak je služba/aplikácia spustená vo virtuálnom stroji. Zmazanie a vytvorenie kontajnera nanovo je totiž výrazne rýchlejšia operácia ako v prípade reštartovania celého virtuálneho stroja. Zmazať a znovu vytvoriť virtuálny stroj môže trvať aj hodiny. 

* V tomto prípade treba zvoliť iný prístup - napr. pomocou **Watch dog**-u.


### Health Checks Interval

* V rámci kontroly zdravia služby, sa _Health Check API_ dopytuje v pravidelných intervaloch. Môže to robiť ďalšia monitorovacia služba alebo orchestračný nástroj, ako je napr. _Kubernetes_.

* Samozrejme k problému môže dôjsť vtedy, ak služba zlyhá medzi dvoma kontrolami. Takže k odhaleniu zlyhania nedôjde okamžite pri jeho vzniku, ale až pri ďalšej kontrole.


## Health Check in Kubernetes Cluster

* ak sa rozprávame o nasadení niektorej služby v K8s klastri, ten na kontrolu stavu používa dve sondy, resp. dva typy kontroly zdravia služieb:

    * **readiness**
    * **liveness**

* Je dôležité rozumieť ako ich rozdielu, tak aj tomu, kedy ich použiť.


### Readiness Probe

* A **readiness** probe is used to indicate whether the process can handle requests (is routable).

  Kubernetes nebude posielať požiadavky pod-u, pokiaľ tento nebude pripravený. Ak táto kontrola neskôr zlyhá, K8s prestane tomuto pod-u posielať požiadavky, pokiaľ znova nebude pripravený.

  Kubernetes doesn't route work to a container with a failing readiness probe. A readiness probe can fail if a service isn't finished initializing, or is otherwise busy, overloaded, or unable to process requests.

  The kubelet uses readiness probes to know when a container is ready to start accepting traffic. A Pod is considered ready when all of its containers are ready. One use of this signal is to control which Pods are used as backends for Services. When a Pod is not ready, it is removed from Service load balancers.


### Liveness Probe

* A **liveness** probe is used to indicate whether the process is to be restarted.

  Táto kontrola povie K8s, či vaša aplikácia funguje (alive) alebo nie (dead). Ak aplikácia funguje, tak ju K8s nechá na pokoji. Ak však nefunguje, K8s pod zmaže a spustí nový, ktorý nefungujúci pod nahradí.

  Kubernetes stops and restarts a container with a failing liveness probe. Use liveness probes to clean up processes in an unrecoverable state, for example, if memory is exhausted, or if the container didn't stop properly after an internal process crashed.

  The kubelet uses liveness probes to know when to restart a container. For example, liveness probes could catch a deadlock, where an application is running, but unable to make progress. Restarting a container in such a state can help to make the application more available despite bugs.


### Responses Provided

| State     | Readiness      | Liveness              | Health |
|           | Non-OK causes no load | Non-OK causes restart | Non-OK causes restart |
|-----------|----------------|-----------------------|---------------------- |
| Starting  | 503 - Unavailable | 200 - OK | Use delay to avoid test |
| Up        | 200 - OK      | 200 - OK              | 200 - OK |
| Stopping  | 503 - Unavailable | 200 - OK | 503 - Unavailable |
| Down      | 503 - Unavailable | 503 - Unavailable |  503 - Unavailable |
| Errored   | 500 - Server Error | 500 - Server Error | 500 - Server Error |


### Types of Probes in K8s

* tri typy:

    1. HTTP
    2. Command
    3. TCP

* Pre overenie *readiness* alebo *liveness* je možné použiť kotrýkoľvek z nich.


#### HTTP Probes

* Najčastejšie používaný typ sondy.

* K8s pingne cestu a keď dostane status kód `2xx`, bude ho považovať za zdravý. V opačnom prípade bude považovaný za nezdravý.

* ukážka

    ```yaml
    spec:
      containers:
      - name: liveness
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8080
    ```


#### Command Probes

* V prípade command probe spustí K8s príkaz vo vnútri bežiaceho kontajnera. Ak spustený príkaz skončí so návratovým kódom `0`, bude kontajner považovaný za zdravý. V opačnom prípade bude považovaný za nezdravý.

* Tento typ je užitočný vtedy, ak nechcete alebo nemôžete spustiť HTTP server, ale stav viete jednoducho overiť spustením príkazu.

* ukážka:

  ```yaml
    spec:
      containers:
      - name: liveness
        livenessProbe:
          exec:
            command:
            - myprogram
    ```


#### TCP Probes

* K8s sa pokúsi vytvoriť spojenie na zadanom porte. Ak sa spojenie podarí vytvoriť, je kontajner považovaný za zdravý. V opračnom prípade je považovaný za chybný.

* Tento typ je užitočný vtedy, ak vám nevyhovuje použitie ani jedného z predchádzajúcich typov. Napr. _gRPC_ alebo _FTP_ služba. 

* ukážka:

  ```yaml
    spec:
      containers:
      - name: liveness
        livenessProbe:
          tcpSocket:
            port: 8080
    ```


#### Configuring Probes

* sondy je možné konfigurovať rozličnými spôsobmi:

    * `initialDelaySeconds` - Dôležitý pre liveness sondu. Liveness sonda sa nemôže pustiť skôr, ako je aplikácia pripravená. V opačnom prípade sa bude aplikácia neustále reštartovať a nikdy nebude pripravená. 
    * `periodSeconds`
    * `timeoutSeconds`
    * `successTreshold`
    * `failureTreshold`

* Pre viac info treba pozrieť dokumentáciu.


## Summary

* health check je požiadavka na každý distribuovaný systém

    * zvyšujú spoľahlivosť
    * zvyšujú dostupnosť

## Additional links

* [Pattern: Health Check API](https://microservices.io/patterns/observability/health-check-api.html)
* [Using a health check in Node.js apps](https://cloud.ibm.com/docs/node?topic=node-node-healthcheck)
* [FastAPI Health](https://github.com/Kludex/fastapi-health)
* [py-healthcheck](https://pypi.org/project/py-healthcheck/)
* Youtube: [Kubernetes Health Checks with Readiness and Liveness Probes](https://www.youtube.com/watch?v=mxEvAPQRwhw)
* [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
