# Lab 2 – Svar

## Del 1

### Nivå 1 – Klassa svarstiden

Indata: En svarstid i millisekunder som ett heltal.
Utdata: En bedömning av svarstiden.

Pseudokod:
1. Läs in svarstiden och omvandla den till ett heltal.
2. Om svarstiden är mindre än 0: skriv "Ogiltigt värde".
3. Annars om svarstiden är mindre än 50: skriv "Utmärkt".
4. Annars om svarstiden är mindre än 150: skriv "Bra".
5. Annars om svarstiden är mindre än 500: skriv "Långsam".
6. Annars: skriv "Ingen användbar kontakt".

### Test av nivå 1

| Svarstid | Förväntat | Faktiskt | OK? |
|---|---|---|---|
| 12 | Utmärkt | Utmärkt | Ja |
| 49 | Utmärkt | Utmärkt | Ja |
| 50 | Bra | Bra | Ja |
| 149 | Bra | Bra | Ja |
| 150 | Långsam | Långsam | Ja |
| 500 | Ingen användbar kontakt | Ingen användbar kontakt | Ja |
| -3 | Ogiltigt värde | Ogiltigt värde | Ja |

## Del 2: Feltabell

## Del 3: Debuggern

## Del 4: Refaktorering