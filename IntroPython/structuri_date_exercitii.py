# Exercitii:

# 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do Afiseaz-o Inversează ordinea folosind
# slicing si suprascrie aceasta lista Printeaza varianta actuala (inversata) Pe aceasta lista, aplica o metoda care
# banuiesti ca face același lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii în acest caz,
# deoarece metoda face asta automat) Printeaza varianta actuala a listei. Practic ai ajuns înapoi la varianta
# inițială Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o
# salvezi intr-o listă nouă. Metoda gasita de tine face suprascrierea automat și permanentizeaza aceste modificări.
# Ambele variante își găsesc utilitatea în funcție de ce ne dorim in acel moment.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# a
print(note_muzicale)
# b
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
# c
note_muzicale.reverse()
print(note_muzicale)

# 2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
print(note_muzicale.count('do'))

# 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista_noua = lista1 + lista2
print(f"Lista unita cu varianta 1 este: {lista_noua}")

lista1.extend(lista2)
print(f"Lista unita cu varianta 2 este: {lista1}")

# 4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista folosind o functie si
# apoi afiseaza din nou lista
lista_noua.sort()
print(f"Lista sortata este: {lista_noua}")
lista_noua.remove(0)
print(f"Lista sortata dupa stergerea numarului 0 este: {lista_noua}")

# 5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
# Lista este goala (IF)
# Lista nu este goala (ELSE)
if len(lista_noua) >= 1:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# 6. Foloseste o functie care sa goleasca lista de la exercitiul 3
lista_noua.clear()

# 7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala
if len(lista_noua) >= 1:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa afisezi Elevii (cheile)
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5}
print(dict1.keys())

# 9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
# Ex: ‘Ana a luat nota {x}’.
# Doar nota o vei lua folosindu-te de cheie
print(f'Ana a luat nota: {dict1["Ana"]}')
print(f'Gigel a luat nota: {dict1["Gigel"]}')
print(f'Gigel a luat nota: {dict1.get("Dorel")}')

# 10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# Modifica nota lui Dorel in 6
# Printeaza nota lui dupa modificare
dict1['Dorel'] = 6
print(dict1.get('Dorel'))

# 11. Imagineaza-ti ca Gigel se transfera din clasa.
# Cauta o functie care sa il stearga
# Vine un coleg nou.
# Adaugati-l in lista pe Ionica, cu nota 9
# Printati dictionarul cu noii elevi
dict1.pop('Gigel')
print(f"Dictionarul dupa transferul ul lui Gigel: {dict1}")
dict1['Ionica'] = 9
print(f"Dictionarul dupa transferul ul lui Ionica: {dict1}")

# 12. Ai urmatoarele seturi:
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
# Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.


zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(f"Lista a ramas identica pentru ca nu se pot afisa duplicate: {zile_sapt}")

# 13. Foloseste un if si verifica daca:
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt
if weekend.issubset(zile_sapt):
    print('weekend este un subset al zilelor sapt')
else:
    print('weekend NU este un subset al zilelor sapt')

# 14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu sunt in weekend si
# invers)
diferenta1 = zile_sapt.difference(weekend)
diferenta2 = weekend.difference(zile_sapt)
print(f"Diferenta dintre zile_sapt si weekend este: {diferenta1}")
print(f"Diferenta dintre weekend si zile_sapt este: {diferenta1}")

# 15. Afiseaza intersectia elementelor din aceste 2 seturi
intersectia = zile_sapt.intersection(weekend)
print(f"Intersectia dintre cele doua seturi este: {intersectia}")

"""
Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google).
"""
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
# Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe  teren
# Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
# Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori de rezerva
# Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele variabilelor voastre)
# Daca jucatorul pe care vrem sa il schimbam nu e in teren:
# Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Altfel, afisati ecran: ‘mai aveti z schimbari’


SCHIMBARI_MAXIME = 3
schimbari_efectuate = 2
# calculam si initializam schimbari ramase
schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
lista_jucatori_teren = ['j1', 'j2', 'j3', 'j4', 'j5']
lista_jucatori_rezerva = ['j6', 'j7', 'j8', 'j9', 'j10']
lista_jucatori_scosi = []
jucator_in = 'j6'
jucator_out = 'j1'

# daca jucatorul e in tere SI daca mai am schimbari
if jucator_out in lista_jucatori_teren and schimbari_ramase > 0:
    if jucator_in in lista_jucatori_rezerva and jucator_in not in lista_jucatori_teren:  # eliminam cazul cand jucatorul este deja in teren
        lista_jucatori_teren.remove(jucator_out)  # scoatem jucatorul
        lista_jucatori_scosi.append(jucator_out)
        lista_jucatori_teren.append(jucator_in)  # adaugam jucatorul nou
        lista_jucatori_rezerva.remove(jucator_in)
        schimbari_ramase = schimbari_ramase - 1  # contorizam schimbarea
        print(f'Schimbare efectuata cu succes!')
        print(f'A intrat {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari')
else:
    if schimbari_ramase <= 0:
        print('Nu mai ai schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')
print(f'Actuala echipa este {lista_jucatori_teren}')
print(f"Jucatorii care au fost scosi sunt: {lista_jucatori_scosi}")
