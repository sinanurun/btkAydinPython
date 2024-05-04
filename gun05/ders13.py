
class Kedi():
    ayak = 4
    kuyruk = True
    def __init__(self,ad):
        self.ad = ad

    @classmethod
    def miyav(cls):
        print("Miyavvvv")

    def yurume(self):
        print("5 adım atti")

tekir = Kedi("Sarman")
print(tekir.ad)
tekir.miyav()
print(tekir.kuyruk)
print(Kedi.kuyruk)
Kedi.miyav()
tekir.yurume()
