# Ett program som håller koll på enheters IP-adresser.
import ipaddress

while True:
    try:
        natet = input("Ange nätverk, till exempel 192.168.10.0/24: ")
        natet = ipaddress.ip_network(natet)
        print("Nätverket är godkänt")
        break
    except ValueError:
        print("Ogiltigt nätverk. Skriv till exempel 192.168.10.0/24.")