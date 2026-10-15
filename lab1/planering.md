# Lab 1 – Planering

## Problem 1

### Steg 1: Förstå
- **Vad är indata?** Platskod (text), Enhetstyp (text) och Senaste använda nummer (heltal).
- **Vad är utdata?** Ett sammansatt och formaterat hostnamn (text) för nästa enhet, till exempel "sto-srv-08".
- **Vilka regler gäller?** Platskod och enhetstyp måste göras om till små bokstäver. Delarna ska sättas ihop med bindestreck. Det nya numret (senaste numret + 1) måste formateras med två siffror.
- **Vad kan gå fel?** Användaren kan skriva in bokstäver istället för siffror eller mata in ett nummer som bryter tvåsifferformatet.

### Steg 2: Planera
LÄS IN platskod
LÄS IN enhetstyp
LÄS IN senaste_nummer
BERÄKNA nästa_nummer = senaste_nummer + 1
BERÄKNA formaterat_nummer = nästa_nummer med två siffror
BERÄKNA hostnamn = platskod (små bokstäver) + "-" + enhetstyp (små bokstäver) + "-" + formaterat_nummer
SKRIV UT "Nästa hostnamn: " + hostnamn

### Steg 4: Testa
| Platskod | Typ | Senaste nr | Förväntat | Faktiskt | OK? |
|---|---|---|---|---|---|
| STO | srv | 7 | sto-srv-08 | sto-srv-08 | Ja |
| gbg | SW | 11 | gbg-sw-12 | gbg-sw-12 | Ja |
| sto | srv | 0 | sto-srv-01 | sto-srv-01 | Ja |
| mal | pc | 99 | mal-pc-100 | mal-pc-100 | Nej |
| sto | srv | sju | Krasch | ValueError | Nej |

- **Vad händer med testet mal, pc, 99?** Hostnamnet blir `mal-pc-100`, vilket bryter regeln om tre delar med två siffror i numret. Företaget borde införa en regel/validering för vad som händer när numret överstiger 99.
- **Vilket fel ger det sista testet?** Det ger ett `ValueError` eftersom koden inte kan omvandla textsträngen `"sju"` till ett heltal med `int()`.

---

## Problem 2

### Steg 1: Förstå
- **Vad är indata?** Filstorlek i GB (decimaltal) och bandbredd i Mbit/s (decimaltal).
- **Vad är utdata?** Överföringstid i sekunder och minuter.
- **Vilka regler gäller?** 1 GB = 1000 MB. Formeln är: tid (s) = (storlek (GB) * 1000 * 8) / bandbredd (Mbit/s).
- **Vad kan gå fel?** Användaren kan mata in 0 som bandbredd, vilket leder till division med noll.

### Steg 2: Planera
Räknat exempel för hand (1 GB på 100 Mbit/s):
tid (s) = (1 * 1000 * 8) / 100 = 8000 / 100 = 80.0 sekunder.

### Steg 4: Testa
| Storlek (GB) | Bandbredd (Mbit/s) | Förväntat (s) | Förväntat (min) | Faktiskt | OK? |
|---|---|---|---|---|---|
| 1 | 100 | 80.0 | 1.33 | 80.0 s / 1.33 min | Ja |
| 4.5 | 250 | 144.0 | 2.4 | 144.0 s / 2.4 min | Ja |
| 50 | 1000 | 400.0 | 6.67 | 400.0 s / 6.67 min | Ja |
| 0.5 | 1000 | 4.0 | 0.07 | 4.0 s / 0.07 min | Ja |
| 1 | 0 | Krasch | Krasch | ZeroDivisionError | Nej |

- **Vilket fel ger det sista testet, och varför?** Det ger `ZeroDivisionError` eftersom koden försöker dela med 0, vilket är matematiskt odefinierat.
- **Två skäl till att överföringen tar längre tid i verkligheten:**
  1. Protokoll-overhead (extra data i paket-headers för TCP/IP).
  2. Nätverksstörningar, paketförluster eller flaskhalsar hos hårdvara/routrar.

---

## Problem 3

### Steg 1: Förstå
- **Vad är indata?** Subnätets prefixlängd (heltal) och antal befintliga enheter (heltal).
- **Vad är utdata?** Totalt antal adresser, användbara adresser och lediga adresser.
- **Vilka regler gäller?** Totalt antal adresser = 2^(32 - prefix). Användbara adresser = totalt - 2.
- **Vad kan gå fel?** Ogiltiga prefixlängder (t.ex. > 32 eller negativa tal).

### Steg 2: Planera
1. Beräkna `hostbitar = 32 - prefix`.
2. Beräkna `totala_adresser = 2 ** hostbitar`.
3. Beräkna `anvandbara = totala_adresser - 2`.
4. Beräkna `lediga = anvandbara - enheter`.

### Steg 4: Testa
| Prefix | Enheter | Förväntat totalt | Förväntat användbara | Förväntat lediga | Faktiskt | OK? |
|---|---|---|---|---|---|
| 24 | 180 | 256 | 254 | 74 | 256 / 254 / 74 | Ja |
| 26 | 50 | 64 | 62 | 12 | 64 / 62 / 12 | Ja |
| 30 | 2 | 4 | 2 | 0 | 4 / 2 / 0 | Ja |
| 16 | 1000 | 65536 | 65534 | 64534 | 65536 / 65534 / 64534 | Ja |
| 27 | 40 | 32 | 30 | -10 | 32 / 30 / -10 | Nej |
| 33 | 0 | Meningslöst | Meningslöst | Meningslöst | Negativt tal | Nej |

- **Test 3 (/30-nät):** Ett /30-nät har exakt 2 användbara IP-adresser, vilket är perfekt för punkt-till-punkt-länkar mellan två routrar utan att slösa på adresser.
- **Test 5 (40 enheter i /27):** Det finns bara 30 användbara adresser, vilket ger -10 lediga. Adresserna räcker inte till alla enheter.
- **Test 6 (prefix 33):** IPv4 har bara 32 bitar totalt. Prefixlängder måste vara mellan 0 och 32 (eller max 30 för vanliga enhetsnät).

---

## Del 4: Från källkod till körning

### Uppgift A: Källkoden i lagringen
- **Sökväg:** `C:\Users\gabri\programmering\lab1\problem3.py`
- **Plats & Avstängning:** Filen ligger sparad på datorns hårddisk/SSD (sekundärminne). När datorn stängs av finns filen kvar eftersom lagringen är permanent (icke-flyktig).

### Uppgift B: Exekveringsmiljön
- **Sökväg till tolken:** `C:\Users\gabri\AppData\Local\Programs\Python\Python315\python.exe`
- **Python-version:** Python 3.15.0
- **Tolkens roll:** Python-tolken läser källkoden, översätter den till bytekod och exekverar instruktionerna steg för steg så att datorns hårdvara förstår vad som ska göras.

### Uppgift C: Operativsystemet och hårdvaran
- **Minnesanvändning (RAM):** Ca 10–15 MB.
- **Vem startade processen:** Operativsystemet (via VS Code/terminalen).
- **När programmet avslutas:** Operativsystemet stänger ner processen och frigör arbetsminnet (RAM). Variablerna rensas helt ur minnet.

### Uppgift D: Sammanfattning
När man klickar på körknappen läser operativsystemet in filens källkod från hårddisken. Operativsystemet skapar en ny process i arbetsminnet och startar Python-tolken. Tolken översätter Python-koden till bytekod som sedan exekveras av processorn (CPU). Under tiden programmet körs lagras variabler och tillfälliga data i datorns arbetsminne. När beräkningarna är klara skickar operativsystemet resultattexten till skärmen, varpå processen avslutas och arbetsminnet frigörs.