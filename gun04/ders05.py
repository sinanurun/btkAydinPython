import datetime
import time
# print('Hello World!')
# # time.sleep(5)
# print('Goodbye!')

a = input("Enter a number: ")
giris = datetime.datetime.now()
print(giris)
b = input("Enter another number: ")
cikis = datetime.datetime.now()
print(cikis)
fark = cikis - giris
print(fark)
print(fark.total_seconds())