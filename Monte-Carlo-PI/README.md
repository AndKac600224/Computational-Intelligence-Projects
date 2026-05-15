średnia z wartości dla $N=10000$ iteracji wszystkich 10 procesów. Na wykresie widoczna jest zmienność estymacji od początku każdej iteracji aż do jej finału wraz z wartością rzeczywistą liczby $\pi$ (czarna prosta).

**Wykresy typu ramka-wąsy dla każdego zestawu 10 finalnych estymacji dla każdego N**

![Wykresy typu ramka-wąsy](assets/boxplots.png)
*(Rys. 3.6)*

Powyżej przedstawione są wykresy typu Boxplot jako zobrazowanie rozkładu wartości dla 10 finalnych estymacji $\pi$ dla każdego $N$ (tzn. zostało przeprowadzone 10 procesów Monte Carlo dla $N=100$ i z 10 finalnych wartości wykonano wykres ramka-wąsy, potem dla $N=1000$ itd.). Dodatkowo na wykres nałożono prostą jako obraz rzeczywistej wartości $\pi$ (dla porównania).

## Etap 4. Wnioski
Podsumowując, przeprowadzony proces estymacji liczby $\pi$ za pomocą algorytmu Monte Carlo wykazał, iż, zgodnie z przewidywaniami, wraz ze wzrostem iteracji $N$ wartość wyliczana jest coraz bliższa prawdziwej tj. ok. 3.141592. W wyniku losowania współrzędnych punktów z rozkładu równomiernego, dla kolejnych wartości parametru $N$ poszczególne obszary (ćwiartka koła oraz ćwiartka układu współrzędnych) są coraz bardziej pokryte w równomierny sposób (rys. 3.1-3.4), co oznacza, że wyliczany iloraz (zgodnie ze wzorem 1.1) jest coraz bardziej wiarygodny względem rzeczywistej wartości $\pi$.

Takie samo zjawisko jest widoczne na wykresie 3.5, gdzie dla każdej z 10 przeprowadzonych serii dla $N=10000$, każda droga dąży ostatecznie do wartości teoretycznej mimo różnych początków (małe $N$). 

Dodatkowo rozbieżność ta jest widoczna na ostatnim wykresie (3.6), gdzie rozkład wartości przedstawiony za pomocą wykresów Boxplot jest definitywnie coraz węższy wraz ze wzrostem ilości iteracji $N$ i coraz bliższy medianą do wartości teoretycznej, co po raz kolejny świadczy o wzroście wiarygodności wartości estymowanej dla coraz większej ilości losowań. 

Ostatecznie otrzymany wynik (dla $N=100000$) różni się od prawdziwej wartości o mniej niż 0.01, zatem algorytm wykazał się pełną użytecznością do tego typu symulacji. Monte Carlo, mimo swojego leniwego podejścia, jest bardzo dobrym narzędziem do rozwiązywania błahych zadań (jak estymacja liczby $\pi$), jak i do bardzo złożonych problemów.
