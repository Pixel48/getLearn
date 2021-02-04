# getLearn <!-- omit in toc -->
[![_last-commit]][last-commit]
[![_commit-activity-m]][commits] <!-- [![_all-contributors]][contributions] -->
[![_languages-count]][tags]
[![_repo-size]][zip]
[![_license]][license]

## Spis treści <!-- omit in toc -->
- [Główne założenia projektu](#główne-założenia-projektu)
- [Lista kategorii rozwijanych i planowanych projektów](#lista-kategorii-rozwijanych-i-planowanych-projektów)
- [Przydatne linki](#przydatne-linki)
  - [Strony internetowe](#strony-internetowe)
  - [Serwery Discord](#serwery-discord)
  - [Repozytoria GitHub](#repozytoria-github)
- [Współpraca](#współpraca)
  - [Jak zacząć?](#jak-zacząć)
  - [Co dalej?](#co-dalej)
  - [Pull request vs Direct access](#pull-request-vs-direct-access)
  - [Jak uzyskać bezpośredni dostęp?](#jak-uzyskać-bezpośredni-dostęp)
    - [Wprowadzaj zmiany](#wprowadzaj-zmiany)
    - [Prowadź wykłady](#prowadź-wykłady)
    - [Pomagaj innym](#pomagaj-innym)
    - [Bądź ogarnięty](#bądź-ogarnięty)
    - [Nie bądź dzbanem](#nie-bądź-dzbanem)
    - [Archiwizuj](#archiwizuj)

## Główne założenia projektu
[getLearn](https://github.com/Pixel48/getLearn) ma pomóc w  zbiorowej i zdecentralizowanej nauce oraz archiwizacji i opracowania przez społeczność materiałów do nauki, zarówno dla pasjonatów chcących aktywnie rozwijać się w kierunkach informatycznych, jak i dla osób, które po prostu chcą zdać swoje egzaminy

~~Repozytorinum podzielone jest na segmenty tematyczne, a każdy z nich opatrzony jest własną menu projektów, omawiający wybraną technologię czy temat~~
> Not Ready Yet

Projekt ma być dynamicznym archiwum rozwijającym się z biegiem lat, służyć jako baza wiedzy i poligon doświadczalny, nadzorowany przez osoby obeznane z technologią wykorzystywaną w rozwijanych projektach. Nadzór ten będzie rozszerzany i przekazywany w miarę rozrastania się repozytorium o kolejne projekty, języki programowania i technologie

Osoby zainteresowane aktywnym udziałem w rozwój projektu zapraszamy do sekcji [***Współpraca***](#współpraca)

## Lista kategorii rozwijanych i planowanych projektów
  - [x] [Matura](/matura/)
    - [x] [R. Infomatyka](/matura/inf/)
    - [ ] R. Matematyka
  - [x] [Egzaminy kwalifikacji zawodowych](/ee/)
    - [ ] EE.09
    - [x] [EE.08](/ee/08/)
    - [ ] EE.03
  - [x] [Nauka programowania](/programming/)
    - [x] [C++](/programming/cpp/)
    - [ ] Python
    - [ ] JavaScript
    - [ ] PHP
    - [ ] SQL
  - [ ] Nauka pracy z git
    - [ ] git
    - [ ] GitHub
    - [ ] Markdown
    
## Przydatne linki
### Strony internetowe
  - [ARKUSZE.PL/informatyka](https://arkusze.pl/informatyka-matura-poziom-rozszerzony/)  
    Archiwum arkuszy maturalnych z informatyki

  - [w3schools.com](https://w3schools.com)  
    Obszerna baza wiedzy z zakresu programowania
    
  - [pythontutor.com](https://pythontutor.com)  
    Wizualizacja działania kodu

### Serwery Discord
  - [Do matury](https://discord.gg/3hyj3kXQkt)  
    Przygotowanie do matury

  - [EE.08/EE.09](https://discord.gg/RJMZQEC)  
    Przygotowanie do egzaminów zawodowych (technik - informatyk) 

### Repozytoria GitHub
  - [Paste Into File](https://github.com/EslaMx7/PasteIntoFile)  
    Program dodający do menu kontekstowego opcję wklejenia zawartości schowka bezpośrednio do nowo utworzonego pliku we skazanej lokalizacji

  - [pyinstaller](https://github.com/pyinstaller/pyinstaller)  
    Zamyka skrypty python'a w plikach wykonywalnych Windows'a
  
  - [MATURA-INFORMATYKA](https://github.com/wernexnrs123/MATURA-INFORMATYKA)  
    Oparty o markdown zbiór wiedzy teoretycznej

## Współpraca
### Jak zacząć?
1. Stwórz fork'a repozytorium pod swoim kontem GitHub i sklonuj je na swoją maszynę, do lokalnej kopii repozytorium
   ```git
   git clone https://github.com/Pixel48/getLearn.git
   ```
   > **Note:** Użyj konta, które będziesz mógł udostępnić przez Discord i odwrotnie - [Serwery Discord](#serwery-discord) są dość mocno powiązane z projektem
2. Zmień nazwę domyślnie ustawionej gałęzi `origin` na `fork`, oraz dodaj oryginalne repozytorium jako `origin` (umożliwi to aktualizację fork'a)
   ```git
   git branch -m origin fork
   git branch add origin https://github.com/Pixel48/getLearn.git
   ```
3. Stwórz odchodzącą od gałęzi `origin/develop` gałąź nazwaną według schematu
   ```git
   git checkout origin/develop
   git checkout -b <kategoria>/<podkategoria>/<nazwa_projektu>
   ```
   > **Note:** W nazwach gałęzi staraj się nie używać dużych liter, podkreśleń i spacji. Niektórzy używają git'a w terminalu i nie ma sensu utrudniać im życia

### Co dalej?
1. Napisz lub dodaj pliki swojego projektu i zatwierdzaj kolejne zmiany w repozytorium. Pamiętaj o odpowiednim opisywaniu wprowadzanych zmian
2. Kiedy skończysz połącz gałąź swojego profektu z gałęzią `develop` (pamiętaj o użyciu flagi `--no-ff`)
> **Note:** Pamiętaj również o zaktualizowaniu repozytorium przed włączaniem zmian do `develop`
3. W głównym kataloguodaj projektu napisz plik README.md opisujący twój projekt. W pierwszej linijce umieść jego nazwę według schematu
   ```markdown
   
   ```
4. Na stronie GitHub fork'a stwórz pull request'a z nazwą i opisem prawidłowo... opisującym wprowadzone zmiany

### Pull request vs Direct access
Używając fork'ow i pull request'ów proponujesz wprowadzenie swoich zmian do repozytorium. Użytkownicy z **dostępem bezpośrednim** decydują o ich akceptacji i mogą dodawać zmiany bezpośrednio w repozytorium 

### Jak uzyskać bezpośredni dostęp?
#### Wprowadzaj zmiany
Dodawaj nowe projekty i ulepszaj istniejące. Osoby aktywnie rozwijające projekt na pewno szybko zostaną zauważone

#### Prowadź wykłady
Ucz innych tego, czego potrafisz nauczyć i zapowiadaj swoje lekcje. [Serwery Discord](#serwery-discord) są otwarte dla wszystkich, ale będą bezużyteczne, jeżeli będziemy tylko czekać na nauczyciela

#### Pomagaj innym
Odpowiadaj na pytania, doradzaj, wyjaśniaj. Jeżeli potrafisz pomóc - pomagaj. Szybko staniesz się rozpoznawalny na [serwerach](#serwery-discord) i uzyskasz odpowiednie rangi. Regularnie sprawdzamy, czy w społeczności nie pojawił się ktoś odpowiedni do nadzoru nad projektem

#### Bądź ogarnięty
Używaj prawdziwych nazw plików i nie trzymaj wszystkich kawałków projektu w podstawowym folderze. Nikt nie ma czasu ani ochoty szukać jednego rozwiązania w przydługiej liście ciągów losowych znaków

#### Nie bądź dzbanem
Traktuj innych z szacunkiem, nie używaj przekleństw jako interpunkcji. Bądź otwarty na dyskusje i czerp z krytyki. Nie musisz podnosić kultury dyskusji, ale też jej nie obniżaj

#### Archiwizuj
Jeżeli uczestniczysz w lekcji, nagraj ją (oczywiście **za zgodą nauczyciela**); Jeżeli nauczyciel nie wrzuci projektu do repozytorium, poproś go o pliki (i spytaj, czy ty możesz to zrobić). Nagranie będzie można wrzucić obok świerzego projektu. Dla kogoś to może być kwestia jego *"Być albo nie być"*

## Licencja <!-- omit in toc -->
Projekt objęty jest licencją [GNU GPL 3][license]

[_last-commit]: https://shields.io/github/last-commit/Pixel48/getLearn
[last-commit]: https://github.com/Pixel48/getLearn/commit/master

[_commit-activity-w]: https://img.shields.io/github/commit-activity/w/Pixel48/getLearn
[_commit-activity-m]: https://img.shields.io/github/commit-activity/m/Pixel48/getLearn
[_commit-activity-y]: https://img.shields.io/github/commit-activity/y/Pixel48/getLearn
[commits]: https://github.com/Pixel48/getLearn/commits/master

[_all-contributors]: https://img.shields.io/github/all-contributors/Pixel48/getLearn
[contributions]: https://github.com/Pixel48/getLearn/graphs/contributors

[_languages-count]: https://shields.io/github/languages/count/Pixel48/getLearn
[tags]: https://github.com/Pixel48/getLearn/releases

[_repo-size]: https://shields.io/github/repo-size/Pixel48/getLearn
[zip]: https://github.com/Pixel48/getLearn/archive/master.zip

[_license]: https://shields.io/github/license/Pixel48/getLearn
[license]: https://github.com/Pixel48/getLearn/blob/master/LICENSE