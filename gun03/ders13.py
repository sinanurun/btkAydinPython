treng = {"araba":"car","kırmızı":"red","kapı":"door"}
print(treng)
print(treng["araba"])
print(treng.keys())
print(treng.values())
print(type(treng))
print(treng.items())
for k,v in treng.items():
    print(k,v)
for dd in treng:
    print(treng[dd])
    print(dd,treng.get(dd))