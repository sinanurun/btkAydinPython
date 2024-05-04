def sayiyazdir(a,b=3,*args):
    print(args)
    print([*args])
    print(a,b,args,sep="\n")
    for sayi in [*args]:
        print(sayi)



sayiyazdir(1,2,3,5,6,4,8,9)