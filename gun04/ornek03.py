yemekler = {"çorbalar":{"etli":["işkembe","kelle","tavuk suyu"],
                        "etsiz":["mercimek","ezo gelin"],
                        "sebze":["domates","brokoli"]},
            "kebaplar":{"acılı":["adana","beyti"],
                        "acısız":["urfa","mardin"],
                        "dürümler":["ciğer","adana"]}
            }

# print(yemekler["çorbalar"]["etli"])
yemekler["çorbalar"]["sebze"].append("Kara Lahana")

yemekler["kebaplar"]["dürümler"].remove("adana")
for anakategori in yemekler:
    print(anakategori) # yemekler sözlüğünün keyleri
    # print("\t", yemekler[anakategori]) # yemeklerin ilk value değerleri yani alt kategoriler
    for altkategori in yemekler[anakategori]:
        print("\t",altkategori)
        for yemek in yemekler[anakategori][altkategori]:
            print("\t\t",yemek)