inloggningar = [3, 0, 5, 1]
misslyckade = 0
timmar_med_larm = 0
for antal in inloggningar:
    misslyckade = misslyckade + antal
    if antal >= 3:
        timmar_med_larm = timmar_med_larm + 1
print("Misslyckade totalt:", misslyckade)
print("Timmar med larm:", timmar_med_larm)