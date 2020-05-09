def pronadji(niz,podatak):
    br = 0
    for i in niz:
        if(i == podatak):
            br += 1
    return br

def dodaj(niz,el):
    niz.append(el)

def umetni(niz,p,u):
    if(p-1 > len(niz)):
        print("Pozicija koju te uneli, je veca nego cela lista.")
    
    niz.insert(p-1,u)

def obrisi(niz,obrisan):
    for i in niz:
        if(i == obrisan):
            niz.remove(obrisan)

def DaLiImaDuplikat(niz):
    for i in niz:
        if(niz.count(i) > 1):
            return True
        else:
            return False

def prviDuplikat(niz):
    for i in niz:
        if(niz.count(i) > 1):
            print("Prvi element koji se ponavlja : ", i)
            break
        else:
            print("nema elemenata koji se ponavljaju.")
            break

niz = [1,6,3,9,5]

for i in range(len(niz)):
    print(niz[i])

niz.reverse()
print(niz)

podatak = int(input("unesite broj koji zelite da pronadjete: "))
print("podatak se pojavljuje : ",pronadji(niz,podatak)," puta")
rl = int(input("unesite le. koji zelite da dodate: "))
print("posle dodavanja na kraj liste: ")
dodaj(niz,rl)
print(niz)

umetak = int(input("unseite element koji zelite da stavite: "))
pozicija = int(input("A sada unesite ispred koje pozicije zelite da dodate element: "))
print("posle umetnog elementa: ")
umetni(niz,pozicija,umetak)
print(niz)

obrisan = int(input("Unesite elemnt koji biste obrisali iz liste: "))
obrisi(niz,obrisan)
print(niz)

if(DaLiImaDuplikat(niz)):
    print("U listi brojeva ima duplikata.")
else:
    print("U listi brojeva nema duplikata.")

prviDuplikat(niz)