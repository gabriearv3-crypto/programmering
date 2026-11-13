# Ett program som håller koll på enheters IP-adresser.
import ipaddress
# Visar ett meddelande när programmet avslutas.
def avsluta():
    print("Programmet avslutas")

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
        print("Här ska vi lägga till enheter senare")
    elif val == "2":
        print("Här ska vi visa enheter senare")
    elif val == "3":
        avsluta()
        break
    else:
        print("Fel val. Skriv 1, 2 eller 3.")