
def Giris():
    islem = int(input("Not girmek için 1 \nNotları okumak için 2\n"))
    
    if(islem ==1):
        notGir()
 
    if(islem == 2):
        NotlariOku()

def NotlariOku():
    with open("bilgiler.txt","r",encoding="utf-8") as file :
        for satir in file:
            print(not_hesapla(satir))
            
def not_hesapla(satir):
        oku =open("bilgiler.txt",'r')
        print(oku.read())
        
              
                    

def notGir():
    ad = input("Öğrenci adı :")
    soyad = input("Ögrenci adı:")
    not1 = input("Not 1 :")
    not2 = input("Not 2 :")
    not3 = input("Not 3 :")
    
    with open("bilgiler.txt","a",encoding="utf-8") as file:
        file.write(ad + ' ' + soyad +' :' +not1+','+not2+','+not3+'\n')
        
    Giris()
     
Giris()