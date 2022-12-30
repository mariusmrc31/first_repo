import random

# Exerciții:


# Ex:1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

"""
daca conditie = True
    se executa acest bloc de cod
altfel
    se executa acest bloc de cod
"""

# Ex:2 - Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg
# mai mare ca 0)
x = 3
if x >= 0 and type(x == int):
    print(f"{x} este un numar natural.")
else:
    print(f"{x} nu este un numar natural.")

# Ex:3 - Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
x = 5
if x > 0:
    print('Numarul este pozitiv')
elif x < 0:
    print('Numarul este negativ')
else:
    print('Numarul este neutru')

# Ex:4 - Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval)
x = 3
if -2 <= x <= 13:
    print('Acest numar este curpins intre -2 si 13. ')
else:  # aceasta cerinta nu era specificata in exercitiu
    print('Acest numar nu este cuprins intre -2 si 13')

# Ex:5 - Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = 13
y = 8
if x - y < 5:
    print('Diferenta este mai mica decat 5.')
else:
    print('Diferenta nu este mai mica decat 5')

# Ex:6 - Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
x = 4
if not (5 <= x <= 27):
    print('Numarul nu este intre 5 si 27.')

# Ex:7 - Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu,
# afiseaza care din ele este mai mare
x = 9
y = 9
if x == y:
    print("Numerele x si y sunt egale.")
elif x > y:
    print(f"{x} este valoarea lui x si este mai mare decat y.")
else:
    print(f"{y} este valoarea lui y si este mai mare decat x.")

# Ex:8 - Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi,
# afiseaza daca triunghiul este isoscel (doua laturi sunt egale),
# echilateral (toate laturile sunt egale)
# sau oarecare (nicio latura nu e egala).
x = 4
y = 4
z = 4
if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print('Triunghiul este isoscel.')
elif x == y == z:
    print('Triunghiul este echilateral.')
else:
    print('Triunghiul este oarecare.')

# Ex:9 - Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu
letter = input('Introduceti o litera: ')
letter = letter.lower()
if letter.isdigit():
    print('Nu ai introdus o litera, ci altceva.')
elif letter.upper() == 'a' or letter.upper() == 'e' or letter.upper() == 'i' or letter.upper() == 'o' or letter.upper() == 'u':
    print('Litera este vocala.')
else:
    print('Litera nu este vocala.')

# Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = float(input("Care este nota primita? "))
if 9 < nota <= 10:
    nota = "A"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 8:
    nota = "B"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 7:
    nota = "C"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 6:
    nota = "D"
    print(f"Nota primita in sistemul american este {nota}")
elif nota > 4:
    nota = "E"
    print(f"Nota primita in sistemul american este {nota}")
elif 4 >= nota >= 0:
    nota = "F"
    print(f"Nota primita este {nota}")
else:
    print('Nu a-ti introdus o nota de la 0 la 10.')

# Exerciții opționale:

# Ex:1 - Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = -999
if 999 < x or x >= 10000:
    print('nu are 4 cifre')
else:
    print('are 4 cifre')

# Ex:2 - Verifica daca x are exact 6 cifre
x = 125645
if len(str(x)) == 6:
    print('are 6 cifre')
else:
    print('nu are 6 cifre')

# Ex:3 - Verifica daca x este numar par sau impar
x = 44
if x % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul este impar.")

# # Ex:4 Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele
x = 4
y = 4
z = 2
if x >= y and x >= z:
    print(f'{x} este cel mai mare numar')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare numar')
else:
    print(f'{z} este cel mai mare numar')

# Ex:5 -  Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este
# valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade sau daca suma lungimilor a
# oricare doua laturi este mai mare decat lungimea celei de-a treia laturi)
x = 5
y = 8
z = 3
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid.')

# Ex:16 Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de la tastatura un număr
# x de tip int și afișează stringul fără ultimele x caractere.
# ex: dacă ați ales 7 se va afisa urmatorul string:
# 'Coral is either the stupidest animal or the smarte'

string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Alege cate caractere vrei sa tai de la final'))
print(string[0:-x])

# Ex:17
'''
Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din primele 5 caractere + ultimele 5
'''
string = 'Coral is either the stupidest animal or the smartest rock'
string1 = string[0:5]
string2 = string[-5:]
print(f'{string1}{string2}')

# Ex:18
'''
Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start al cuvântului rock - 
                    adică poziția in string la care începe cuvântul rock (hint: este o funcție care te ajuta sa faci asta). 
                    Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant. 
                    Output asteptat: 'Coral is either the stupidest animal or the smartest ' 
'''
string = 'Coral is either the stupidest animal or the smartest rock'
index_rock = string.index('rock')
print(string[:index_rock])

# Ex:9 Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se va folosi un
# assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA' e acceptat ca un string in care
# primul si ultimul caracter este la fel (hint, te poti folosi de o functie pentru a face string-ul case insensitive)
word = input('alege un str')
# assert word[0].lower() == word[len(word)-1].lower(), 'Primul si ultimul caracter sunt diferite'

# Ex: 10 Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare (hint: foloseste
# slicing si controleaza afisarea in slicing cu slicing step)
word = '0123456789'
print(word[0::2])
print(word[1::2])

"""
Exerciții Bonus 
"""

# 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept inputuri urmatoarele
# informatii: Varsta Insotit de mama Insotit de tata Pasaport Act permisiune mama Act permisiune tata Conditii de
# imbarcare: Daca pers are varsta peste 18 ani si are pasaport Daca pers are sub 18 ani, are pasaport si e insotita
# de ambii parinti Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in
# scris de la celalat parinte Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu
# toate variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si apoi ruleaza
# codul pentru a verifica daca expected results sunt egale cu actual results.
# Exemple:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca

varsta = int(input("Va rugam sa introduceti varsta pasagerului "))
pasaport_valid = input("E pasaportul valid? Da/Nu ")
if varsta >= 18 and pasaport_valid == "Da":
    print("Va puteti imbarca")
elif varsta < 18 and pasaport_valid == "Da":
    ambii_parinti = input("E copilul insotit de ambii parinti? ")
    if ambii_parinti == "Da":
        print("Va puteti imbarca")
    else:
        permisiune = input("Permisiune parinte lipsa: ")
        if permisiune == "Da":
            print("Va puteti imbarca")
        else:
            print("Nu va puteti imbarca")
else:
    print("Nu va puteti imbarca")

"""
Scenarii de testare:
1. Adult peste 18 ani cu pasaport valid => Se poate imbarca
2. Adult peste 18 ani cu pasaport invalid => Nu se poate imbarca
3. Copil cu pasaport valid si ambii parinti => Se poate imbarca
4. Copil cu pasaport valid si un singur parinte - permisiune parinte lipsa => Se poate imbarca
5. Copil cu pasaport valid si un singur parinte - fara permisiune parinte lipsa => Nu se poate imbarca
6. Copil fara pasaport valid => Nu se poate imbarca
"""

# 2. Joc de noroc Cauta pe net si vezi cum se genereaza un numar random Imagineaza-ti ca dai cu zarul si salvezi
# acest numar intr-o variabila numita dice_roll. Numarul salvat va fi generat random cu metoda gasita in online
# Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator Verifica si afiseaza daca
# utilizatorul a ghicit numarul Vor exista 3 optiuni care vor trebui tratate: Ai pierdut. Ai ales un numar mai mic.
# Ai ales x dar a fost y Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y Ai ghicit. Felicitari? Ai ales
# x si zarul a fost y


dice_roll = random.randint(0, 6)
guess = int(input('Ghiceste zarul'))
if guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}')
elif guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {guess} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {guess} si zarul a fost {dice_roll}')

# Exercitii extra:

# Exercitiul 1 ####
# Creaza 2 variabile de tip string, primua cu valoarea "veni vidi vici" si a doua cu valoarea "alea iacta est"
# a) Afiseaza cate caractere are primul string
# b) Afiseaza cate caractere are al doilea string
# c) Elimina spatiile albe din primul string

str1 = "veni vidi vici"
str2 = "alea iacta est"
print(len(str1))
print(len(str2))
print(str1.split())

# Exercitiul 2 ####
# Creaza variabila s1 de tip string si asigneaza-i valoarea "veni vidi vici"
# a) Foloseste o metoda string astfel incat sa se afiseze veni, vidi, vici
# b) Creeaza o noua variabila de tip string in care sa stochezi numarul de "i" care apar in s1 si afiseaza-i valoarea.
# c) Inlocuieste in s1 litera "v" cu litera "a"

s1 = "veni vidi vici"
s2 = s1.count("i", 0, 14)
print(s2)
print(s1.replace("v", "a"))

# Exercitiul 3 ####
# Citeste un string format din 6 litere de la tastatura si afiseaza litera de pe pozitia 4.
s1 = input("Introdu un cuvant format din 6 litere ")
print(s1[4])

# Exercitiul 4 ####
# Avem variabila x = "astazi am avut o sedinta lunga si obositoare"
# Foloseste o metoda string astfel incat propozitia sa inceapa cu litera mare.
x = "astazi am avut o sedinta lunga si obositoare"
print(x.capitalize())

# Exercitiul 5 #### Citeste de la tastatura un string format din 3 cuvinte (exemplu: am plecat azi) a) Afiseaza o
# parte din string care sa contina ultimile 2 litere din al doilea cuvant si prima litera din al treilea cuvant,
# fara sa contina spatii albe intre ele b) Transforma stringul obtinut la punctul a) intr-un string care contine
# numai litere mari
str = input("Introdu o propozitie din 3 cuvinte ")
print(str.upper())

# Exercitiul 6 ####
# Creeaza cate o variabila tip string pentru fiecare zi a saptamanii (exemplu: day02="Tuesday")
# a) Afiseaza toate zilele saptamanii pe un singur rand cu virgula intre ele.
# b) salveaza stringul obtinut la punctul b) intr-o variabila
# c) Afiseaza pe ce pozitie se regaseste prima litera din Sunday
# d) Afiseaza cate litere are Sunday

d1 = "Monday"
d2 = "Tuesday"
d3 = "Wednesday"
d4 = "Thursday"
d5 = "Friday"
d6 = "Saturday"
d7 = "Sunday"
saptamana = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
print(saptamana)
print(saptamana.find("Sunday"))
print(len("Sunday"))


# Exercitiul 1 ####
# Afisati in consola rezultatul expresiei:  10 * 100 - (2**3 + 6 ** 2) - 290
a = 10 * 100 - (2**3 + 6 ** 2) - 290
print(a)

# Exercitiul 2 #### Afiseaza in consola rezultatul lui 24 la puterea a 3-a (i.e Rezultatul lui 24 la puterea a 3-a
# este: ). Folositi un output formatat.
x = 24 ** 3
print(f"Rezultatul lui 24 la puterea a 3-a este {x}")

# Exercitiul 3 ####
# Sa se calculeze si sa se afiseze in consola n la puterea 7, unde n este citit de la tastatura.
n = int(input("Introdu un numar "))
print(n**7)

# Exercitiul 4 #### Avem 2 numere intregi citite de la tastatura. Daca valoarea primului numar este mai mare decat
# valoarea celei de-al doilea, atunci sa se afiseze in consola "I have a dog". Daca nu este mai mare, atunci sa se
# afiseze "I have a cat".
a = int(input("Numar "))
b = int(input("Numar "))
if a > b:
    print("I have a dog")
else:
    print("I have a cat")

# Exercitiul 5 ####
# Avem 2 numere intregi citite de la tastatura.
# Creeaza variabila x si asigneaza-i valoarea 3.
# Aduna numerele introduse de la tastatura si rezultatul afiseaza-l ridicat la puterea valorii lui x.
a = int(input("Numar "))
b = int(input("Numar "))
x = 3
y = a + b
print(y**x)

# Exercitiul 6 ####
# Avem a = 0, b = 1, c = 0, d = 1
# Afiseaza ce returneaza urmatoarea operatie not(a or b and c or d)
a = 0
b = 1
c = 0
d = 1
print(not(a or b and c or d))  # => False

# Exercitiul 7 ####
# Avem s = 1 si x = 0
# Ce operator/i punem intre s si x daca vrem sa obtinem True? - 2 modalitati.
s = 1
x = 0
print((s or x))
print(not(s and x))


# Exercitiul 1 #### a) Sa se citeasca de la tastatura un cuvant. b) Sa se verifice daca cuvantul introdus de la
# tastatura are toate literele mari. Daca nu are toate literele mari, atunci sa se converteasca cuvantul in litere
# mari.
str = input("Introdu un cuvant ")
print(str.isupper())
print(str.upper())

# Exercitiul 2 #### a) Sa se citeasca de la tastatura 3 numere. b) Sa se determine daca cele 3 numere sunt pare. Daca
# cele 3 numere sunt pare, atunci sa se afiseze "Toate numerele sunt pare" Daca fie si unul dintre numere este impar,
# atunci sa se afiseze "Nu toate numerele sunt pare"
a = int(input("Numar "))
b = int(input("Numar "))
c = int(input("Numar "))
if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("Toate numerele sunt pare")
else:
    print("Nu toate numerele sunt pare")

# Exercitiul 3 #### a) Sa se citeasca de la tastatura un string b) Sa se determine daca numarul caracterelor
# stringului citit de la tastatura este mai mare de 6. Daca numarul este mai mare decat 6, atunci sa se afiseze
# "Numarul de caractere este mai mare decat 6", altfel "Numarul este mai mic decat 6".
my_str = input("scrie ceva ")
if len(my_str) > 6:
    print("Numarul de caractere este mai mare decat 6")
else:
    print("Numarul este mai mic decat 6")


# Exercitiul 4 ####
# a) Sa se creeze un log in cu username si parola introduse de la tastatura
# b) Sa se compare valorile. Pentru fiecare caz afisam urmatoarele:
# Caz1: user corect - parola gresita -> "Wrong password"
# Caz2: user gresit - parola corecta -> "Wrong username"
# Caz3: user gresit - parola gresita -> "Wrong username and password"
# Caz4: user si parola corecte -> "Logged in"
user = "Madalina"
user1 = input("Introdu user-ul: ")
parola = "Madalina"
parola1 = input("Introdu parola: ")
if user1 == user and parola1 != parola:
    print("Wrong password")
elif user1 != user and parola1 == parola:
    print("Wrong username")
elif user1 != user and parola1 != parola:
    print("Wrong username and password")
else:
    print("Logged in")
