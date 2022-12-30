# Curs 8

# Encapsulare = este o metoda prin care putem sa atribuim un anumit nivel de acces unor variabile sau metode
# niveluri de acces:
# - public - sunt vizibile de oriunde din program
# - protected (_) -> se pot folosi doar in aceeasi clasa sau si in clasa
# - private (__)-> se pot folosi doar in interiorul clasei curente

# restrictionarea accesului
# information hiding - ascundem anumite aspecte despre codul nostru pentru cei din exterior
# prezinta in schimb o interfata pe care ceilalti o pot folosi, fara a stii ce face codul intern

# Toti membrii intr-o clasa Python sunt public by default
# Orice membru poate fi accesat de oriunde din program

# Private members #####
# __(dubllu underscore) este prefixul pentru variabile private
# nu trebuie foloiste in afara clasei.

class Car:

    def __init__(self, wheel, speed, color):  # definim constructorul
        self.__wheel = wheel  # private class atribute
        self.__speed = speed  # private class atribute
        self.__color = color  # private class atribute

    def __print_me(self):
        print("I am a private method")


renault = Car("right", 180, "green")
# print(renault.__color)
# Orice incercare de a folosi atributul in afara clasei va rezulta intr-o eroare --> AttributeError
# print(renault.__print())

# python face o modificare a variabilelor private.
# Fiecare membru cu __ o sa fie schimbat in _object.class_variable --> poate fi accesat in afara clasei
# DAR NU TREBUIE SA FACEM ASTA
# print(dir(renault))

# Cum se acceseaza - REFRAIN FROM DOING SO
print(renault._Car__speed)
renault._Car__speed = 500
print(renault._Car__speed)


# Python nu are  un mecanism care sa restrictioneze accessul pe metode sau variabile
# Pur si simplu exista conventia de a folosi _ si __ care sa simuleze comportamentul de protected si private
# Ramane la latitudinea dezvoltatorului sa inteleaga acest lucru.

# Protected members ########## protected members - sunt accesibili in interiorul clasei cat si in subclase. Nu pot fi
# accesati din oriuce alta parte instance variable protected --> _var_name (single underscore). Folosind underscore,
# previne sa fie accesat, mai putin daca e accesat dintr-o subclasa


# Transformam clasa Car

class Car:

    def __init__(self, wheel, speed, color):  # definim constructorul
        self._wheel = wheel  # protected class atribute
        self._speed = speed  # protected class atribute
        self._color = color  # protected class atribute

    def get_speed(self):
        return self._speed

    def get_color(self):
        return self._color

    def get_wheel(self):
        return self._wheel

    # set a new color
    def set_color(self, value):
        self._color = value

    def set_speed(self, value):
        self._speed = value


# daca scrie in felul asta, nu previne variabilele instantei sa acceseze sau sa modifice instanta


peugeot = Car("right", 240, "white")  # nu ne da eroare cand scriem valorile
# print("peugeot color: ", peugeot.color)
print("peugeot color:", peugeot._color)

# Daca vrem sa modificam culoarea
peugeot.color = "black"  # nu schimba culoarea
peugeot._color = "black"
print(peugeot._color)

# Daca o variabila jeste scrisa cu underscore(este protected), programatorul se va ABTINE sa o modifice in afara clasei

# setam culoarea apeland metoda de setare a culorii
peugeot.set_color("Black")
print(peugeot.get_color())


# Avem un exemplu cu clasa Car cu toate atributele publice. Putem accesa si modifica valorile oricand

class Car:

    def __init__(self, wheel, speed, color):  # definim constructorul
        self.wheel = wheel
        self.speed = speed
        self.color = color

# Accesam atributele publice


kia = Car("right", 200, "white")  # cream o instanta/obiect al clasei Car folosindu-ne de atribute
ford = Car("left", 180, "blue")  # cream o instanta/obiect al clasei Car folosindu-ne de atribute
mitsubishi = Car("right", 240, "cameleon")  # cream o instanta/obiect al clasei Car folosindu-ne de atribute

print(f"Viteza maxima a masinii Mitusbishi este {mitsubishi.speed}")

# putem modifica valoarea vitezei masinii Mitsubishi
mitsubishi.speed = 220

print(f"Viteza maxima a masinii Mitsubishi este acum de {mitsubishi.speed}")