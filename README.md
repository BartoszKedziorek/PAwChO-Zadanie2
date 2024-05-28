### Konfiguracja łańcucha CI

![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/0368aa56-c293-409c-8085-293a2cc7352c)

Etykiety ```push``` oraz ```workflow_dispatch``` wskazują opowienio na to, że łańcuch CI będzie wykonywany w
przypadku wypychania commitów do repozytorium oraz w przypadku ręcznego uruchomienia.<br /><br />


![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/7af81cc2-5f9c-4d3f-9cae-5462b025f555)

W realizowanym przykładzie utowrzony został jeden łańcuch CI. Etykieta ```runs-on``` pozwala na zdefiniowanie maszyny
na, której będą wykonywane operacje. W realizowanym przykładzie do wykonania akcji wykorzystany zostnie
kontener z obrazem ubuntu w najnowszej wersji.<br /><br />


![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/9f59da5d-667e-410f-8019-20583fc6a37a)

Sekcja permissions definiuje uprawnienia akcji.<br />
```contents: read``` - uprawnienie odczytu zawartości repozytorium<br />
```packages: write``` - uprawnienie zapisu do ghcr<br />
```attestations: write``` - uprawnienie zapisu artefaktów atestacji<br /><br />


![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/10f12b97-3928-4d58-8aa0-9bd63ce789e0)

```steps``` - etyieta oznaczająca sekcję w której definiowane będą kroki dla wybranej akcji.<br /><br />


![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/38e8149d-4ec6-43c5-a58f-ab5b387f0102)

Pierwsze trzy kroki odpowiadją odpowiednio za: sprawdzenie czy akcja ma dostęp do repozytorium, ustawienie qemu
na kontenerze akcji oraz utworzenie buildera.<br /><br />


![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/b323f643-154b-43e7-b0ce-56988e6a8070)

Akcja służąca logowaniu do githuba.<br /><br />


![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/f3ebd499-89f9-4aa6-b339-6636a8394d61)

Kolejne dwie akcje budują obraz lokalnie oraz sprawdzają go pod względem ewentualnych podatności. Dla polecenia
docker scout użyte zostały flagi ```--exit-code``` oraz ```--only-severity```. Flaga ```--only-severity```
pozwala na określenie poziomów podatności na które uwagę ma zwracać polecenie, natomiast flaga
```--exit-code``` w przypadku wykrycia podatności, powoduje zwrócenie kodu 2 przez polecenie
oraz przerwanie wykonywania dalszych kroków.<br /><br />


![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/e4391d55-c75b-4a10-8253-d4d95564a212)

Akcja ta służy do pobierania metadanych na temat obrazu.<br /><br />


![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/c9803672-3931-4302-8e5b-066ae6c30e30)

Akcja budująca obraz oraz wypychająca go do zdalnego repozytorium obrazów (ghcr.io)<br /><br />

### Wynik działania
![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/094f752d-06b1-443f-b36e-ae98a1f22664)

![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/1d51907d-87dd-4988-bb64-4facf750da6d)
<br /><br />

### Wyjaśnienie


![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/6b882c5b-a49c-4764-baff-d0f03679a958)



Podczas realizaji zadania napotkałem na problem. Polecenie ```docker scout cves``` wskazuje, iż w obrazie z zadania 1.
znajduje się jedna podatność o stopniu wysokim [link](https://scout.docker.com/v/CVE-2018-20225?s=gitlab&n=pip&t=pypi&vr=%3E%3D0).
Niestety ale ```pip``` nie posiada aktualnie wersji, która rozwiązuje tę kwestię. Dlatego właśnie nie dokońca zgodnie
z poleceniem zadania, obraz jest wypychany do repozytorium tylko w przypadku gdy nie zawiera on błędów krytycznych
(przepuszcza obrazy z błędami o stopniu wysokim). Zmiana ta wprowadzona zotsała w celu przetestowania całego łańcucha.
Aby łańcuch wypychał do zdalnego repozytorium obrazy, które nie zawierają błędów krytycznych oraz wysokich wystarczy
jako argument flagi ```--only-severity``` podać ```high,critical```. Polecenie w łańuchu będzie wtedy miało postać:<br /><br />
![image](https://github.com/BartoszKedziorek/pawcho-zadanie2/assets/104023013/e1145d28-6b6c-4952-a89b-df9fb6f3dc1d)



