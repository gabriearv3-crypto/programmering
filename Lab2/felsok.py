# Rapport över diskanvändning på servrarna
enheter = ["srv-01", "srv-02", "srv-03", "srv-04"]
disk = [45, 92, 80, 67]
GRANS = 80


def rakna_over_grans(varden, grans):
    antal = 0
    for varde in varden:
        if varde >= grans:
            antal = antal + 1
    return antal


def medelvarde(varden):
    summa = 0
    for i in range(0, len(varden)):
        summa = summa + varden[i]
    return summa / len(varden)


print("Rapport för", len(enheter), "enheter")
print("Medel:", round(medelvarde(disk), 1))
print("Minst 80 %:", rakna_over_grans(disk, GRANS))
print("Största värde:", max(disk))
print("Sista enheten:", enheter[3])