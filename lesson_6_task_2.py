class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def pavement_mass(self, spec_grav, thick):
        return self._length * self._width * spec_grav * thick / 1000

mass = Road(5000, 20)

print(mass.pavement_mass(25, 5))


