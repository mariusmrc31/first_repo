# Curs 7

# Mostenirea
# mostenirea se foloseste cand avem 2 sau mai multe clase similare
# cream clasele Cat and Dog
# cream o clasa generala numita Pets
# clasa parinte
class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what sounds I make")


# clasa copil
class Cat(Pets):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    # def speak(self):
    #     print("Meeeeow")


# clasa copil
class Dog(Pets):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def speak(self):
        print("Bark")


# class child Fox mosteneste class parinte Pets
class Fox(Pets):
    pass


fox = Fox("Snow", 1)
fox.speak()

# create an object that belongs to Cat class
cat = Cat("Billy", 3, "blue")

# create an object that belongs to Dog class
dog = Dog("Black", 5, "Shnautzer")
#
# cat.speak()
# dog.speak()

pet = Pets("Mike", 19)  # cream o instanta a clasei Pet
pet.speak()
cat.speak()


# create classes
# cream o clasa Dog si scriem atributele clasei Dog
# definim o clasa Dog folosing cuvantul cheie class

class Dog:
    ####
    def __init__(self, name, age):
        # trebuie sa accesam numele undeva pt a fi accesar mai tarziu
        self.name = name
        self.age = age

    def bark(self):
        print("Ham ham!")

    def sad(self):
        print("I am sad")

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age


d = Dog("Billy", 5)
print(type(d))  # returneaza <class '__main__.Dog'> este un obiect al clasei Dog
# avem __ pt a ne arata in ce modul clasa a fost definita.
# by default modulul pe care l-ai rulat este modulul prinicpal
# de unde si denumirea __main__

d.bark()  # utilizam o metoda pe o instanta a clasei dog

# aplicam metoda sad pe obiectul d
d.sad()
print(d.get_name())

d2 = Dog("Oreo", 12)
print(d2.get_name())
d2.set_age(2)
d.set_age(2)


# mai sus am facut un blueprint pentru clasa dog
# avem un sistem de gestiune universiar


class Person:
    def __init__(self, age, weight, height, first_name, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name


# cream o noua persoana (o instanta a clasei Person)
# putem accesa atributele clasei si sa le folosim la persoana pe care vrem sa o cream,


user = Person(25, 65, 150, "Akihkio", "Takayama")
print(user.height)  # ne arata
print(type("hello"))


# avem functia
def greetings():
    print("Hello there human!")


print(type(greetings))  # de verificat


# methods
mystring = "yellow there"
print(mystring.upper())  # --. metoda care actioneaza asupra unui obiect
# print(s.upper())
