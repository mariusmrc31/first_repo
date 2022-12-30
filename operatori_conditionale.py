# CURS 2

# STRING METHODS #############

# .capitalize( ) ####
# modifica stringul astfel incat prima litera va fi mare si restul literelor vor fi mici
# syntax: str.capitalize()
myStr = "casa mea este Mica"
print(myStr.capitalize())

# .endswith() ####
# verifica daca un string se termina cu litera data ca argument
# syntax: str.endswith("something")
myStr = "casa mea este Mica"
print(myStr.endswith("ca"))

# .find( ) ####
# cauta un substring si returneaza indexul unde se gaseste
# este safe - nu returneaza o eroare daca ii dam un substring nonexistent ca parametru, cu -1
# functioneaza numai cu stringuri - nu incercati sa o aplicati pe alte secvente

# find() with one parameter ##
# syntax: str.find("substring")
my_string = "invat python"
print(my_string.find("at"))

# find() with 2 parameters ##
# if you want to search the substring starting with a certain index
# syntax: str.find("substring", poz)
my_string = "astazi nu vreau sa invat"
print(my_string.find("zi", 2))
fructe = "mere pere caise"
print(fructe.find("er"))

# find() with 3 parameters
# al treilea argument pointeaza catre primul index care nu va fi luat in considerare in cautare
# syntax: str.find("substring", poz, poz_end_search)
nume = "Maria Ioana Angelica Ion"
print(nume.find("Angelica", 0, 20))

# .isalnum() ####
# verifica daca un string contine numai litere si cifre. Returneaza un bool -> True / False
mother = "Cristina10"
print(mother.isalnum())

# .isalpha() ####
# verifica daca un string este format numai din litere si returneaza True / False
# syntax: str.isalpha()
# spatiile nu sunt considerate litere, sunt considerate caractere
my_string = "Am ani"
print(my_string.isalpha())

# .isdigit() ####
# verifica daca un string este format numai din numere
# syntax: str.isdigit()
varsta = "28"
print(varsta.isdigit())

# .islower() ####
# verifica daca un string este format numai din litere mici si returneaza True / False
# syntax: str.islower()
litera_mica = "am plEcat in vacanta"
print(litera_mica.islower())

# .isspace() ####
# verifica daca stringul este format numai din spatii goale si returneaza True / False
# syntax: str.isspace()
spatiu = "am plecat"
spatiu2 = "   "
print(spatiu.isspace())
print(spatiu2.isspace())

# .isupper() ####
# verifica daca un string este format numai din litere mari si returneaza True / False
# syntax: str.isupper()

# .lower() #### face o copie a stringului original si inlocuieste toate literele mari din string cu litere mici si
# returneaza noul string ca rezultat the original string remains untouched. syntax: str.lower()

# .upper() #### face o copie a stringului original si inlocuieste toate literele mici din string cu litere mari si
# returneaza noul string ca rezultat the original string remains untouched. syntax: str.upper()

# replace() #### retruneaza o copie a stringului original in care toate aparitiile primului argument au fost
# inlocuite cu al doilea argument syntax: str.replace(arg1, arg2)

my_str = "cainele ma musca"
print(my_str.replace("cainele", "pisica"))

# exercitiu: ce returneaza urmatorul cod
s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)
# Answer:

# split() ####
# aceasta metoda considera ca stringurile sunt delimitate de spatii albe
# syntax str.split()
# example: print("phi       chi\npsi".split()) -> ['phi', 'chi', 'psi']
ex = "bujori flori trandafiri"
print(ex.split())

# strip() ####
# returneaza un nou string fara spatii albe
# syntax: str.strip()

# exercitiu: ce returneaza urmatorul cod?
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)
print(s2[-2])
# Answer: of
# ex 2
a = "Tomorrow I will leave my home"
b = a.split()
print(b)
print(b[-4])

# swapcase() ####
# returneaza un nou string in care tipul de litere este inversat. litere mici -> litere mari , viceversa

s = "i WaS a BaD CaT"
print(s.swapcase())

# OPERATORI ARITMETICI ###############

# Addition
a = 5
b = 275
c = 1985

print(a + b + c)

# Substraction

print(c - a + b)

# Multiplication
print(a * b)

# Division
a = 20
b = 10
print(a / b)

# Modulus
a = 5
b = 2
print(a % b)

# Exponentiation
a = 2
b = 3
print(a ** b)

# OPERATORI DE ATRIBUIRE #############

# " = "
a = 5
b = 888

# " += "
a = 6
a += 5  # a = a + 5 => a = 6 + 5
print(a)

# " -= "
b = 110
b -= 10  # => b = 110 - 10
print(b)

# " *= "
c = 3
c *= 2  # =>c = 3 * 2
print(c)

# " /= "
d = 22
d /= 11  # d = 22 /11
print(d)

d = 11
d /= 7
print(round(d))

# OPERATORI LOGICI #############

# "and"
# returns TRUE if both statements are true
a = 0
b = 1
print(a and b)

# "or"
# returns true if one of the statements is true
c = 0
d = 0
print(c or d)

# "not"
e = 1
b = 6
print(not (b < e))
n = 10
s = 12
x = 2
print(not (n * 2 < s < 15))  # => not( 20 < 12  and 12 < 15) => not( False and True ) => not (False) => True

# OPERATORI DE COMPARARE #############
# string comparison is always case-sensitive --> upper-case letters are taken as lesser than lower-case letters.
# OBS! - nu comparam 2 tipuri diferite de date cu comparatorii <, > <=, >=, primim eroare "TypeError "


# " == "
a = 12
c = 10
print(a == c)

# " != "
print(a != c)

# " > "
print(a > c)

# " < "
a = 12
c = 10
print(a < c)

# " >= "
s = 199
n = 200
print(n >= s)

# " <= "
print(n <= s)

# if statament #####

# condition not fullfieled
a = 70
b = 10
c = a * b
if c > 1000:
    print("Yay valoarea lui c este mai mare decat 1000")
print(f"c are valoarea {c}")

# condition fullfilled
if c < 1000:
    print("valoarea lui c este mai mica decat 1000")
print(f"{c}")

# if..else statements ####
a = "mama"
b = "Mama"
if a == b:
    print("Mama si cu tata merg la restaurant")
else:
    print("Mama sta acasa")

# if else if statements ####
a = 12
b = 3
c = 3
s = b % c

if s == 0:
    print("s is an even number")
elif s < 2:
    print("S este mai mic decat 2")
elif b > c:
    print("b este mai mare decat c")
else:
    print("s este numar impar")
print("Se continua codul")

# ex 2
fruct1 = "pere"
fruct2 = "Pere"
alt_str = "tanculete"

if fruct1 == fruct2:
    print("Facem dulceata de pere")
elif fruct1 != alt_str:
    print("Nu mai facem dulceata")
else:
    print("I don't care")
print("Ai ajuns aici")

# nested if else statements ####
nr1 = 24
nr2 = 25
s1 = "mama"
s2 = "mama"

if nr1 > nr2:
    if s1 == s2:
        print("conditia s-a indeplinit")
    else:
        print("Nu s-a indeplinit conditia")
else:
    print("Am intrat pe else clause")
