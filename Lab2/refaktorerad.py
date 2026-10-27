GRANS_LANGSAM_MS = 300


def berakna_summa(svarstider):
    total = 0
    for svarstid in svarstider:
        total = total + svarstid
    return total


def rakna_langsamma(svarstider, grans):
    antal = 0
    for svarstid in svarstider:
        # Exakt gränsvärde ska inte räknas som långsamt i denna rapport.
        if svarstid > grans:
            antal = antal + 1
    return antal


svarstider_ms = [120, 95, 310, 80, 450]

total_ms = berakna_summa(svarstider_ms)
medel_ms = total_ms / len(svarstider_ms)
antal_langsamma = rakna_langsamma(svarstider_ms, GRANS_LANGSAM_MS)

print("Total svarstid:", total_ms)
print("Genomsnittlig svarstid:", medel_ms)
print("Antal långsamma svar:", antal_langsamma)