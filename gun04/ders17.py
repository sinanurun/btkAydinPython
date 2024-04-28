def sayiyazdir(a,b=3,*args, c= 45):
    print(args)
    print([*args])
    print(a,b,args,c,sep="\n")
    for sayi in [*args]:
        print(sayi)



sayiyazdir(1,2,3,5,6,4,8,9)