# Współpraca <!-- omit in toc -->
<details>
<summary><u>Spis treści</u></summary>

- [Pull request & Direct access](#pull-request--direct-access)
  - [Jak uzyskać bezpośredni dostęp?](#jak-uzyskać-bezpośredni-dostęp)
    - [Wprowadzaj zmiany](#wprowadzaj-zmiany)
    - [Prowadź wykłady](#prowadź-wykłady)
    - [Pomagaj innym](#pomagaj-innym)
    - [Bądź ogarnięty](#bądź-ogarnięty)
    - [Nie bądź dzbanem](#nie-bądź-dzbanem)
    - [Archiwizuj](#archiwizuj)
</details>

## Jak zacząć?
<details>
<summary><u>Nowy w świecie gita?</u></summary>


</details>

1. Stwórz fork'a repozytorium pod swoim kontem GitHub i sklonuj je na swoją maszynę, do lokalnej kopii repozytorium
   ```git
   git clone https://github.com/Pixel48/getLearn.git
   ```
   > Note: Użyj konta, które będziesz mógł udostępnić przez Discord i odwrotnie - [Serwery Discord](#serwery-discord) są dość mocno powiązane z projektem
2. Zmień nazwę domyślnie ustawionej gałęzi `origin` na `fork`, oraz dodaj oryginalne repozytorium jako `origin` (umożliwi to aktualizację fork'a)
   ```git
   git branch -m origin fork
   git branch add origin https://github.com/Pixel48/getLearn.git
   ```
3. Przejdź do ostatniej zmiany w gałęzi `develop`
   ```git
   git checkout origin/develop
   ```
4. Stwórz odpowiednio nazwaną gałąź:
   - matura
   ```git
   git checkout -b matura-<przedmiot>/<rok>/<miesiąc>
   ```
   - egzamin kwalifikacyjny
   ```git
   git checkout -b ee-<kod_kwalifikacji>
   ```
   -  projekt
   ```git
   git checkout -b <kategoria>/<podkategoria>/<nazwa_projektu>
   ```
   > Note: W nazwach gałęzi staraj się nie używać dużych liter, podkreśleń i spacji. Sporo osób używa gita w terminalu. Nie utrudniajmy im pracy

## Co dalej?
Napisz lub dodaj pliki swojego projektu i zatwierdzaj kolejne zmiany w gałęzi swojego projektu. Pamiętaj o odpowiednim opisywaniu wprowadzanych zmian
   > Note: **NIE ŁĄCZ** swojej gałęzi z innymi - po przyjęciu pull request'a może być potrzebna normalizacja nazw plików, ścierzek i odnośników, aby zachować spójność z resztą repozytorium

## Porządkowanie plików i wysyłanie zmian
### Rozwiązanie arkusza
1. Umieść rozwiązania do arkusza w folderze:  
   `matura/<przedmiot>/<rok>/<miesiąc>/rozwiązanie`
2. Umieść opracowywany arkusz w folderze:  
   `matura/<przedmiot>/<rok>/<miesiąc>/arkusz`
3. Na stronie fork'a utwórz pull request o nazwie `matura-<przedmiot>/<rok>-<miesiąc>`  
   i krótkim opisem

### Rozwiązanie egzaminu kwalifikacyjnego
1. Umieść rozwiązania do arkusza w folderze:  
   `<XX>/<00>/<rok>/<miesiąc>/arkusz <numer arkusza>/rozwiązanie`
2. Umieść arkusz w folderze:  
   `<XX>/<00>/<rok>/<miesiąc>/arkusz <numer arkusza>/arkusz`
3. Na stronie fork'a utwórz pull request o nazwie `<XX>-<00>/<rok>-<miesiąc>/arkusz <numer arkusza>`  
   i krótkim opisem 

### Projekt
1. Umieść pliki projektu w folderze:  
   `<kategoria>/<podkategoria>/<nazwa_projektu>`
2. W głównym katalogu projektu napisz plik README.md opisujący twój projekt
3. Na stronie fork'a utwórz pull request z adekwatną nazwą i krótkim opisem wprowadzonych zmian 

# Pull request & Direct access
Używając fork'ow i pull request'ów proponujesz wprowadzenie swoich zmian do repozytorium. Użytkownicy z **dostępem bezpośrednim** decydują o ich akceptacji i mogą dodawać zmiany bezpośrednio w repozytorium 

## Jak uzyskać bezpośredni dostęp?
### Wprowadzaj zmiany
Dodawaj nowe projekty i ulepszaj istniejące. Osoby aktywnie rozwijające projekt na pewno szybko zostaną zauważone

### Prowadź wykłady
Ucz innych tego, czego potrafisz nauczyć i zapowiadaj swoje lekcje. [Serwery Discord](#serwery-discord) są otwarte dla wszystkich, ale będą bezużyteczne, jeżeli będziemy tylko czekać na nauczyciela

### Pomagaj innym
Odpowiadaj na pytania, doradzaj, wyjaśniaj. Jeżeli potrafisz pomóc - pomagaj. Szybko staniesz się rozpoznawalny na [serwerach](#serwery-discord) i uzyskasz odpowiednie rangi. Regularnie sprawdzamy, czy w społeczności nie pojawił się ktoś odpowiedni do nadzoru nad projektem

### Bądź ogarnięty
Używaj prawdziwych nazw plików i nie trzymaj wszystkich kawałków projektu w podstawowym folderze. Nikt nie ma czasu ani ochoty szukać jednego rozwiązania w przydługiej liście ciągów losowych znaków

### Nie bądź dzbanem
Traktuj innych z szacunkiem, nie używaj przekleństw jako interpunkcji. Bądź otwarty na dyskusje i czerp z krytyki. Nie musisz podnosić kultury dyskusji, ale też jej nie obniżaj

### Archiwizuj
Jeżeli uczestniczysz w lekcji, nagraj ją (oczywiście **za zgodą nauczyciela**); Jeżeli nauczyciel nie wrzuci projektu do repozytorium, poproś go o pliki (i spytaj, czy ty możesz to zrobić). Nagranie będzie można wrzucić obok świerzego projektu. Dla kogoś to może być kwestia jego *"Być albo nie być"*