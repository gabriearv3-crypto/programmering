# Problem 1: Nästa hostnamn

# 1. Läs in data från användaren
platskod = input("Platskod (t.ex. sto): ")
enhetstyp = input("Enhetstyp (t.ex. srv, sw, pc): ")
senaste_nummer = int(input("Senaste använda nummer: "))

# 2. Beräkna nästa nummer och formatera till två siffror
nästa_nummer = senaste_nummer + 1
formaterat_nummer = f"{nästa_nummer:02d}"

# 3. Sätt ihop hostnamnet med små bokstäver och bindestreck
hostnamn = f"{platskod.lower()}-{enhetstyp.lower()}-{formaterat_nummer}"

# 4. Skriv ut resultatet
print(f"Nästa hostnamn: {hostnamn}")