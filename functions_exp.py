def old_sum(a,b):
    return a + b

old_sum(4,3)

#isimsiz fonksiyon
new_sum = lambda a,b : a+b
print(new_sum(4,5))

sirasiz_liste = [("b",3), ('a',8), ('d',12), ('c',1)]
#her bir tuple içineki 1. indexe gidip sıralasın
print(sorted(sirasiz_liste, key= lambda x : x[1]))


#vektörel operasyonlar

#oop
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

print(ab)

#fp fonksiyonel programlama
import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
print(a*b)

#map & filter & reduce
liste = [1,2,3,4,5]

for i in liste:
    print(i + 10)

list(map(lambda x: x + 10, liste)) #map fonksiyonu verilen bir vektörün içerisinde belli bir fonksiyonu çalıştırma imkanı verir

#filter   bir nesne alır ve üzerinden başka bir nesne alır ve istediği elemanları filtreler

liste2 = [1,2,3,4,5,6,7,8,9,10]
filtrele = list(filter(lambda x: x%2 == 0, liste2))
print(filtrele)

#reduce
from functools import reduce #module içerisinden kütüphane çağırdık
liste = [1,2,3,4]
print(reduce(lambda a,b: a+b, liste))