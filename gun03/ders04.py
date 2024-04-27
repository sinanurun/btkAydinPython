pazar = ["elma","armut","erik","çilek","karpuz"]
print(pazar)
print(pazar[3])
print(pazar[:2])
print(pazar[-3:])
print(pazar[::-1])
print(pazar[2:4:])

pazar.append("ananas")
print(pazar)
pazar.append("elma")
print(pazar)
print(pazar.count("elma"))
print(pazar.index("ananas"))
pazar.insert(2,"kiraz")
print(pazar)
pazar[0]= "yeşil Elma"
print(pazar)
pazar.sort()
print(pazar)
pazar.reverse()
print(pazar)
dayipazar = ["şeftali","kayısı"]
pazar.extend(dayipazar)
print(pazar)
amcapazar = ["patates","soğan"]
pazar.append(amcapazar)
print(pazar)
pazar.pop()
print(pazar)
pazar.pop(2)
print(pazar)
del pazar[2]
print(pazar)
pazar.remove("elma")
print(pazar)
pazar.clear()
print(pazar)
ypazar = ["elma"] + ["patates"]
print(ypazar)
ypazar = ypazar *2
print(ypazar)
# del pazar
# print(pazar)

