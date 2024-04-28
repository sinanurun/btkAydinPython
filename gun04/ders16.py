# def daire(r, pi):
#     alan = pi * r * r
#     return alan
#
# print(daire(4,3.14))
def kare(a):
    return a*a
# def daire(r, pi=3.14):
#     alan = pi * kare(r)
#     return alan
# alan = daire(5, 3)
# print(alan)
# print(daire(8))

def daire(r=1, pi=3.14):
    alan = pi * kare(r)
    return alan
alan = daire()
print(alan)
print(daire(8))