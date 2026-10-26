svarstid = int(input("Ange svarstid i ms: "))

if svarstid < 0:
    print("Ogiltigt värde")
elif svarstid < 50:
    print("Utmärkt")
elif svarstid < 150:
    print("Bra")
elif svarstid < 500:
    print("Långsam")
else:
    print("Ingen användbar kontakt")