---
title: Introduction to Microservices
courseid: fastapi
order: 101
layout: lecture
---

## Monolith Approach

* tradicny pristup pri vyvoji softveru je vytvorit monolit

* monolit - vtipne pomenovanie, ak chceme oznacit single element containing everything ;)

* tymto sposobom zacina v podstate kazdy projekt a casto je tento projekt vedeny jednym clovekom alebo mensim timom a neriesi ziadne hranice castami systemu, nakolko je to kontraproduktivne

* monolit samozrejme moze mat velmi dobru internu strukturu a moze byt aj velmi dobre naprogramovany. to, co ho vsak definuje, je poziadavka na jeho nasadenie ako celku bez toho, aby ho bolo mozne nasadit po castiach (partial deployments).

### Monolith Limitations

* ako zacne monolit rast, zacnu sa objavovat niektore jeho obmedzenia:

### the code will increase in size

* bez nejakych striktnych hranic zacnu mat vyvojari problem s pochopenim celeho kodu
* zacne byt problem s rozsirovanim jeho funkcionality a opravovanim vzniknutých chýb
* spustanie testov (ak nejaké su) sa s veľkosťou zacne spomalovat (spolu s rychlostou CI systemu)


### inefficient utilization of resources

* each deployment will require all the resources required for the system to work
* maximum amount of memory for any kind of request
* same applies for CPU
* prístup/spojenie s databázou a to bez ohľadu na to, ci ju potrebuje alebo nie


### issues with development scalability

* aj napriek tomu, ze system moze byt paradne horizontalne skalovatelny, s tym, ako rastie, rastie aj developersky tim. a s nim rastie aj problem "neliezt si do kapusty" :-) 

* maly tim sa koordinuje lahsie, ako velky. duplom v situaciach, ked viacero timov pracuje s jednym zdrojovym kodom (code base). doraz na vzajomnu koordinaciu moze mat za nasledok znizenie ich nezavislosti a rychlosti.


### deployment limitations

* nasadenie systemu/aplikacie si moze zacat vyzadovat pracu viacerych timov. a v pripade vzniku problemu pri nasadzovani systemu, moze byt vysledkom jeho nefunkcnost.


### interdependency of technologies

* kazda nova technologia, ktora je pridana do monolitu, musi zapadnut medzi existujuce pouzivane technologie. takze pridanie novej technologie moze predstavovat komplikaciu kvoli existujucim technologiam.

* rovnako tak moze byt komplikovana aj aktualizacia existujucich technologii na nove verzie. napr. aktualizacia jazyka Python (alebo niektoreho jeho modulu) sa moze tykat celeho zdrojoveho kodu.

* kritickym to moze byt napr. v pripade bezpecnostnych aktualizacii, ked sa tomu proste neda vyhnut ;) pouzivanie specifickej verzie kniznice a jej nasledna aktualizacia si proste vyzaduje extra pracu navyse.


### A bug in a small part of the system can bring down the whole service

este predtym, ako sa dostaneme k tej "najzavaznejsej" chybe, vam poviem jeden pribeh. neviem, kto je autor ani kde som to videl, ale velmi dobre odraza ten najvacsi problem, ktory si so sebou monolit nesie, pretoze je to monolit ;)


### summary

* vo vysledku - kazda jedna kriticka chyba, ktora sa dotyka stability systemu, sa dotyka vsetkeho. a kazda jedna takato chyba vie zabezpecit pad celeho systemu.

* ako je vidiet, problemy s monolitom su narastajuce problemy, ktore rastu s velkostou zdrojoveho kodu. ked je kod maly, su aj tieto potencialne problemy zanedbatelne. ale s rastucou velkostou zdrojoveho kodu rastu aj tieto problemy.

* Takze - ak to mame zhrnut - monolit funguje az do momentu, ked fungovat prestane ;)

* Aka je vsak k nemu alternativa?


## What is Microservice?

Existuje mnoho definicii toho, co je to mikrosluzba (microservice), ale zrejme stale nie je taka, ktora je naozaj uznavana. pozrime sa na dve z nich - jednu kratku a druhu dlhsiu:

> "...a collection of loosely coupled specialized services that work in unison to provide a comprehensive service."
>
> -- Jaime Buelta: Hands-On Docker for Microservices with Python (2019)

tuto kratsiu verziu vieme nájsť v rozličných prevedeniach na viacerých miestach.

pozrime sa ale na to, ako microsluzby opísal Martin Fowler v roku 2014:

> "...is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API. These services are built around business capabilities and independently deployable by fully automated deployment machinery. There is a bare minimum of centralized management of these services, which may be written in different programming languages and use different data storage technologies."
>
> -- James Lewis and Martin Fowler (2014)


## What is REST API?
