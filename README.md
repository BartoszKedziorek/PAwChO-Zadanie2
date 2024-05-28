### Konfiguracja łańcucha CI

![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/0368aa56-c293-409c-8085-293a2cc7352c)
etykiety ```push``` oraz ```workflow_dispatch``` wskazują opowienio na to, że łańcuch CI będzie wykonywany w
przypadku wypychania commitów do repozytorium oraz w przypadku ręcznego uruchomienia..

![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/7af81cc2-5f9c-4d3f-9cae-5462b025f555)
W realizowanym przykładzie utowrzony został jeden łańcuch CI. ```Etykieta runs-on``` pozwala na zdefiniowanie maszyny
na, której będą wykonywane operacje. W realizowanym przykładzie do wykonania akcji zostanie wykorzystany zostnie
kontener z obrazem ubuntu w najnowszej wersji.

![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/9f59da5d-667e-410f-8019-20583fc6a37a)
Sekcja permissions definiuje uprawnienia akcji.
```contents: read``` - uprawnienie odczytu zawartości repozytorium
```packages: write``` - uprawnienie zapisu do ghcr
```attestations: write``` - uprawnienie zapisu artefaktów atestacji

![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/10f12b97-3928-4d58-8aa0-9bd63ce789e0)
```steps``` - etyieta oznaczająca sekcję w której definiowane będą kroki dla wybranej akcji
