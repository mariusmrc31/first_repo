from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    def descriere(self):
        print("Cel mai probabil am colturi")

    @abstractmethod
    def aria(self):
        pass


class Patrat(FormaGeometrica):

    def __init__(self):
        self._latura = 0

    def aria(self):
        return self._latura ** 2

# getter method

    def get_latura(self):
        return self._latura
# setter method

    def set_latura(self, new_value):
        self._latura = new_value
        return self._latura
# deleter method

    def del_latura(self):
        print("Latura este stersa!")
        del self._latura


class Cerc(FormaGeometrica):
    def __init__(self):
        self._raza = 0
# getter method

    def get_raza(self):
        return self._raza
# setter method

    def set_raza(self, new_value):
        self._raza = new_value
        return self._raza
# deleter method

    def del_raza(self):
        print("Raza este stearsa!")
        del self._raza

    def aria(self):
        return FormaGeometrica.PI*self._raza**2

    def descriere(self):
        print("Eu nu am colturi!")


patrat = Patrat()
cerc = Cerc()
print(patrat.get_latura())
patrat.set_latura(10)
print(patrat.get_latura())
print(patrat.aria())
patrat.del_latura()
patrat.set_latura(5)
print(patrat.aria())
cerc.set_raza(3)
print(cerc.get_raza())
cerc.del_raza()
cerc.set_raza(10)
print(cerc.aria())
cerc.descriere()
