# SPRAWOZDANIE Z PROJEKTU FUZZY LOGIC – WSKAŹNIK BMI
**Kacper Andrzejewski**

## 1. Wstęp
Tematem projektu jest wykorzystanie procesów logiki rozmytej i wnioskowania rozmytego do wyznaczania wskaźnika BMI (Body Mass Index). Tradycyjne podejście do BMI opiera się na sztywnych granicach (np. 25.0 to już nadwaga, a 24.99 to waga prawidłowa), co bywa krzywdzące i nie oddaje płynności stanów fizjologicznych. Zastosowanie wnioskowania rozmytego pozwala na uwzględnienie nachodzących na siebie przedziałów, co prowadzi do bardziej naturalnej i precyzyjnej klasyfikacji stanu zdrowia.

## 2. Użyte technologie
* **MATLAB 2024R** – środowisko obliczeniowe.
* **Fuzzy Logic Designer** – rozszerzenie do projektowania systemów rozmytych.
* **System FIS**: Mamdani Type-1.
* **Plik konfiguracyjny**: `mamdanitype1.fis`.

## 3. Teoria
Wskaźnik BMI obliczany jest tradycyjnie według wzoru:

$$
BMI = \frac{M}{H^2}
$$

gdzie:
* $M$ – masa ciała w kilogramach.
* $H$ – wzrost w metrach.

W projekcie logiki rozmytej system nie wykorzystuje bezpośrednio tego wzoru, lecz wypracowuje wynik na drodze wnioskowania z rozmytych przesłanek.

## 4. Przygotowanie systemu rozmytego (FIS)

### Zmienne wejściowe (Inputs)
Zdefiniowano dwie zmienne lingwistyczne:
1. **Waga [kg]**: Zakres [35, 160]. MF: Mała, Średnia, Duża, Bardzo duża.
2. **Wzrost [cm]**: Zakres [140, 215]. MF: Niski, Średni, Wysoki.

### Zmienna wyjściowa (Output)
1. **BMI**: Zakres [10, 50]. MF obejmują stany od wygłodzenia (10-15) do otyłości III stopnia (39.5-50).

### Baza reguł
System opiera się na 12 regułach wnioskowania (kombinacja 3 typów wzrostu i 4 typów wagi). Przykładowo:
* *IF (waga is Średnia) AND (wzrost is Średni) THEN (BMI is Optymalna)*.
* *IF (waga is Mała) AND (wzrost is Wysoki) THEN (BMI is Wygłodzenie)*.

### Defuzzyfikacja
Zastosowano metodę **środka ciężkości (centroid)**, która równomiernie uwzględnia wszystkie aktywowane fragmenty funkcji przynależności, dając płynny wynik liczbowy.

## 5. Analiza działania algorytmu

Poniżej przedstawiono rezultaty wnioskowania dla trzech różnych scenariuszy:

| Przypadek | Parametry | Wynik (BMI) | Wizualizacja |
| :--- | :--- | :--- | :--- |
| **a) Optymalny** | 75 kg, 175 cm | Waga prawidłowa | ![Optymalny](assets/rule5-75-175.png) |
| **b) Skrajny** | 50 kg, 195 cm | Wygłodzenie | ![Skrajny](assets/rule7-50-195.png) |
| **c) Reprezentatywny** | 83 kg, 175 cm | "Rozmyty" (między normą a nadwagą) | ![Rozmyty](assets/rule56-83-175.png) |

W przypadku (c) widać istotę logiki rozmytej – system aktywował dwie reguły jednocześnie (nr 5 i 6), co odzwierciedla stan na granicy przedziałów.

## 6. Reprezentacja przestrzenna (Surface Plots)
Wykresy powierzchniowe obrazują nieliniową zależność wskaźnika BMI od wagi i wzrostu, wynikającą z bazy reguł i kształtu funkcji przynależności.

| Przekrój 1 | Przekrój 2 |
| :---: | :---: |
| ![Surface 1](assets/structure.png) | ![Surface 2](assets/structure2.png) |
| *(Wykres 4)* | *(Wykres 5)* |

## 7. Wnioski
Logika rozmyta pozwala na modelowanie nieprecyzyjnych pojęć lingwistycznych w sposób matematyczny. System BMI w MATLABie udowodnił, że można uzyskać wiarygodne wyniki diagnostyczne bez sztywnego stosowania wzorów, unikając jednocześnie błędów wynikających z ostrych granic decyzyjnych.

---
