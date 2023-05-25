# Zestaw 3

##### OBOWIĄZKOWE DO PRZESŁANIA: wszystko oprócz 3.7
<br>

## Zadanie 3.1
Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
for i in "axby": if ord(i) < 100: print (i)
for i in "axby": print (ord(i) if ord(i) < 100 else i)

## Zadanie 3.2
Co jest złego w kodzie:

L = [3, 5, 4] ; L = L.sort()
x, y = 1, 2, 3
X = 1, 2, 3 ; X[1] = 4
X = [1, 2, 3] ; X[3] = 4
X = "abc" ; X.append("d")
L = list(map(pow, range(8)))

## Zadanie 3.3
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.

## Zadanie 3.4
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

## Zadanie 3.5
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|

0&nbsp; 1&nbsp; 2&nbsp; 3&nbsp; 4&nbsp; 5&nbsp; 6&nbsp; 7&nbsp; 8&nbsp; 9&nbsp; 10&nbsp;11&nbsp;12

## Zadanie 3.6
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+

|&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |

+---+---+---+---+

|&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |

+---+---+---+---+

## Zadanie 3.8
Dla dwóch sekwencji liczb lub znaków znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

## Zadanie 3.9
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

## Zadanie 3.10
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].