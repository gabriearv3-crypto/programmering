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

Kontrollräkning:
(45 + 92 + 80 + 67) / 4 = 284 / 4 = 71.
Två värden är minst 80: 92 och 80.

| Nr | Rad | Feltyp | Hur hittade du felet? | Vad var fel? | Hur rättade du det? | Hur kan felet förebyggas? |
|---|---|---|---|---|---|---|
| 1 | 22 | Syntaxfel | Felmeddelandet | Avslutande citattecken saknades. | Lade till citattecknet efter enheter. | Kontrollera att text har citattecken på båda sidor. |
| 2 | 7 | Syntaxfel | Felmeddelandet | Kolon saknades efter funktionens parentes. | Lade till kolon. | Kontrollera att funktionsdefinitioner avslutas med kolon. |
| 3 | 25 | Exekveringsfel | Felmeddelandet TypeError | Text och heltal slogs ihop med +. | Bytte + mot komma i print. | Kontrollera datatyper och använd komma för att skriva ut text och tal. |
| 4 | 26 | Exekveringsfel | Felmeddelandet IndexError | Index 4 finns inte i listan med fyra enheter. | Ändrade index till 3. | Kom ihåg att listans första index är 0. |
| 5 | 17 | Logiskt fel | Jämförde med förväntad utskrift och granskade loopen. | Loopen började på index 1 och hoppade över första värdet. | Ändrade startvärdet till 0. | Kontrollera att loopen tar med alla värden. |
| 6 | 10 | Logiskt fel | Jämförde med förväntad utskrift och granskade villkoret. | Villkoret > räknade inte med exakt 80. | Ändrade > till >=. | Testa värden precis på gränsen. |

## Del 3: Debuggern

## Del 4: Refaktorering