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
Efter genomgången förväntar jag mig 9 misslyckade
inloggningar totalt och 2 timmar med larm.
| När programmet pausar | antal | misslyckade | timmar_med_larm |
|---|---|---|---|
| Rad 5, varv 1 | 3 | 0 | 0 |
| Rad 5, varv 2 | 0 | 3 | 1 |
| Rad 5, varv 3 | 5 | 3 | 1 |
| Rad 5, varv 4 | 1 | 8 | 2 |
| Rad 8, efter loopen | 1 | 9 | 2 |

### Varför ändras timmar_med_larm inte i varje varv?

timmar_med_larm ändras bara när antal är minst 3.
När antal är 0 eller 1 är villkoret falskt och räknaren ändras inte.
### Vilket värde har antal när loopen är klar? Varför?

antal har värdet 1 eftersom det är det sista värdet i listan.
Variabeln behåller sitt värde efter loopen.
### Stämde min förväntan?

Ja, efter genomgången förväntade jag mig 9 misslyckade
inloggningar och 2 timmar med larm. Det stämde med resultatet.

### Hur kan debuggern hjälpa mig att hitta logiska fel?

Jag kan köra en rad i taget och se hur variablernas värden ändras.
Då kan jag upptäcka om ett värde hoppas över eller om ett villkor
ger fel resultat, även om programmet inte visar något felmeddelande.
## Del 4: Refaktorering