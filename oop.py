class VeriBilimci():
    bolum = ''
    sql = 'evet'
    deneyim_yili = 0
    bildigi_diller = []

#sınıfların özelliklerine erişmek
print(VeriBilimci.bolum)
print(VeriBilimci.sql)

#sınıfların özelliklerini değiştirmek
VeriBilimci.sql="hayır"
print(VeriBilimci.sql)

#sınıf örneklenmesi
ali = VeriBilimci() #bu classın özelliklerini taşıyor. class dan nesne ürettik

ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)
print(VeriBilimci.bildigi_diller)

#örnek özellikleri
#her bir örneğin kendi içinde değişebilen örneklerden oluşur bu sayede
class VeriBilimci():
    bildigi_diller = ["R","Python"]  #veribilimci sınıfının da özelliğini tanımlamış olduk. sadece alttaki kod ile olmuyor yoksa
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''

ali = VeriBilimci()
print(ali.bildigi_diller)

veli = VeriBilimci()
print(veli.bildigi_diller)

ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)
print(veli.bildigi_diller)

veli.bildigi_diller.append("R")
print(veli.bildigi_diller)

print(VeriBilimci.bildigi_diller)


#örnekler üzerinde çalışan fonksiyonlar
class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)

ali = VeriBilimci()
veli = VeriBilimci()

print(dir(VeriBilimci))

ali.dil_ekle("R")
print(ali.bildigi_diller)


#Miras Yapıları
class Employees():
    def __init__(self):
        self.Firstname = ""
        self.Lastname = ""
        self.Address = ""

class DataScience(Employees): #departman  miras yapısı
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience()

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""


mar1 = Marketing()

class Employee_yeni():
    def __init__(self, Firstname, Lastname, Address):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Address = Address

ali = Employee_yeni("a","b","c")
print(ali.Firstname)

