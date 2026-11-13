# Slutprov – IP-register
Gjort av: Gabriell Arvidsson

## Pseudokod
Fråga efter kontorets nätverk
Om nätverket är ogiltigt
    Visa felmeddelande och fråga igen

Skapa en tom lista för enheter

Funktion för att lägga till enhet
    Fråga efter enhetens namn
    Om namnet är tomt
        Visa felmeddelande och fråga igen

    Fråga efter IP adressen
    Om adressen är ogiltig eller ligger utanför nätverket
        Visa felmeddelande och fråga igen

    Spara namnet och den godkända adressen i listan
    Visa att enheten har lagts till

Funktion för att visa alla enheter
    Gå igenom listan med en for loop
    Visa nummer och namn och IP adress för varje enhet

Funktion för att avsluta
    Visa ett avslutningsmeddelande

Upprepa menyn tills användaren väljer att avsluta
    Visa rubriken IP register
    Visa alternativen
        1 Lägg till enhet
        2 Visa alla enheter
        3 Avsluta

    Fråga efter användarens val

    Om valet är 1
        Kör funktionen för att lägga till enhet
    Annars om valet är 2
        Kör funktionen för att visa alla enheter
    Annars om valet är 3
        Kör funktionen för att avsluta
        Avbryt loopen
    Annars
        Visa felmeddelande
## Redogörelse

## AI-logg

## Reflektion

## Testtabell (för A)