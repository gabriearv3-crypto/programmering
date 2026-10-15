# Problem 3: Beräkna nätverksadress

# 1. Läs in IP-adress och nätmask
ip_adress = input("IP-adress: ")
natmask = input("Nätmask (t.ex. 24): ")

# 2. Dela upp IP-adressen i fyra delar
delar = ip_adress.split(".")

# 3. Ersätt sista delen med 0 för att få nätverksadressen
delar[3] = "0"
natverks_ip = ".".join(delar)

# 4. Skriv ut nätverksadressen i CIDR-format
print(f"Nätverksadress: {natverks_ip}/{natmask}")