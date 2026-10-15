# Problem 2: Tidsuppskattning

# 1. Läs in antal enheter
antal_enheter = int(input("Antal enheter: "))

# 2. Beräkna total tid i minuter (15 min start + 10 min per enhet)
total_tid = 15 + (antal_enheter * 10)

# 3. Omvandla till timmar och minuter
timmar = total_tid // 60
minuter = total_tid % 60

# 4. Skriv ut resultatet
print(f"Total tid: {total_tid} minuter")
print(f"Det motsvarar: {timmar} timmar och {minuter} minuter")