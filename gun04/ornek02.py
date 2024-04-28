oyuncular = {"bjk":["muchi","mertens","necip"],
             "gs":["icardi","muslera","zahan"],
             "fb":["tadich","irfancan","ferdi"]}


for i in oyuncular:
    # print(i)
    # print(oyuncular[i])
    # print(i,"takımının oyuncu listesi",oyuncular[i])
    print(i,"takımının oyuncu listesi : ")
    if type(oyuncular[i]) is list:
        for j in oyuncular[i]:
            print( "\t", j)




# print(oyuncular)
# for takim in oyuncular.keys():
#     print(takim)
#
# for takim in oyuncular.values():
#     print(takim)
#
# for takim, kaptan in oyuncular.items():
#     print(takim, kaptan)