# Ett program som håller koll på enheters IP-adresser.
import ipaddress
enheter = []
# Visar alla enheter med nummer, namn och IP-adress.
def visa_enheter(enheter):
    nummer = 1
    for enhet in enheter:
        print(nummer, enhet[0], enhet[1])
        nummer = nummer + 1

# Visar ett meddelande när programmet avslutas.
def avsluta():
    print("Programmet avslutas")
# Kontrollerar namn och IP-adress och sparar enheten.
def lagg_till(natet, enheter):
    while True:
        namn = input("Ange enhetens namn: ").strip()
        if namn != "":
            break
        print("Namnet får inte vara tomt.")

    while True:
        try:
            ip = ipaddress.ip_address(input("Ange IP-adress: "))

            if ip not in natet:
                print("Adressen ligger inte i kontorets nätverk.")
            else:
                enheter.append([namn, str(ip)])
                print("Enheten har lagts till.")
                break

        except ValueError:
            print("Ogiltig IP-adress. Skriv till exempel 192.168.10.20.")
while True:
    try:
        natet = input("Ange nätverk, till exempel 192.168.10.0/24: ")
        natet = ipaddress.ip_network(natet)
        print("Nätverket är godkänt")
        break
    except ValueError:
        print("Ogiltigt nätverk. Skriv till exempel 192.168.10.0/24.")
while True:

    print("IP-register")
    print("1. Lägg till enhet")
    print("2. Visa alla enheter")
    print("3. Avsluta")

    val = input("Välj 1, 2 eller 3: ")

    if val == "1":
        lagg_till(natet, enheter)
    elif val == "2":
        visa_enheter(enheter)
    elif val == "3":
        avsluta()
        break
    else:
        print("Fel val. Skriv 1, 2 eller 3.")