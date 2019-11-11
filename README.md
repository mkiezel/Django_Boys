# Gilded_rose
Projekt zaliczeniowy ZJP UG

### Test
Aby odpalić test uruchom skrypt "test.py" w pythonie 3.
Program poprosi o podanie wersji Gilded_rose, czyli uzupełnienie
"gilded_rose_v**"

### Zmiany
#### v1 -> v2
* usunięcie powrarzającego się kodu sprawdzającego max quality = 50, zmiana na sprawdzanie tego warunku w ostatniej linijce.
* dodanie ominięcia całego przejścia pętli, gdy itemem jest sulfuras, co daje nam możliwość usunięcia wszystkich if, które go zawierały.
#### v2 -> v3
* wyciągnięcie zagnieżdżonego if'a dotyczącego koncertów
* dodanie warunku min quality = 0 na końcu pozwoliło usunąć 5 if'ów w środku kodu
* usunięcie niepotrzebnych warunków
* zmniejszenie maksymalnego zagnieżdżenia o 1 poziom
#### v3 -> v4
* zmiana warunków przeczących na twierdzące (!= -> ==)
#### v4 -> v5
* zmniejszenie maksymalnego zagnieżdżenia warunków do 2 stopnia
* dodanie metody "item_quality_range_check()"
#### v5 -> v6
* dodanie metody "concert_update()"
#### v6 -> v7
* dodanie zmiennej, która pozwoliła usunąć dublujący się kod
