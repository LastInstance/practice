class Vehicle():
    def __init__(self, cost, colour, mark):

        self.cost = cost
        self.colour = colour
        self.mark = mark
    def __str__(self):
        return f'Your choice is {self.mark} and the colour is {self.colour}\nIt cost {self.cost} '


    def __repr__(self):
        return f'Vehicle(\'{self.mark}\', {self.colour}, {self.cost}'


class Moto(Vehicle):
    def speed(self, speed):
        self.speed = speed
        print("Maximum speed of this moto is" , self.speed)
    def cost(self):
        super().cost()
        return f'Cost of this moto is {self.cost}'
    def mark(self):
        super().mark()
        return f'This is {self.mark}'
    def colour(self):
        super().colour()
        return f'His colour is {self.colour}'

class Auto(Vehicle):
    def type(self, type):
        self.type = type
        print("Type of this auto is", self.type)

    def seats(self, seats):
        self.seats = seats
        print ("Number of seats of this auto is", self.seats)

    def mark(self, mark):
        super().mark()
        return f'This is {self.mark}'
    def cost(self, cost):
        super().cost()
        return f'It costs {self.cost}'
    def colour(self, colour):
        super().colour()
        return f'Colour of this auto is {self.colour}'

class Boat(Vehicle):

    def speed(self, speed):
        self.speed = speed
        print('Maximum speed of this boat is', self.speed)

    def type(self, type):
        self.type = type
        return ('Type of this boat is', self.type)

    def cost(self, cost):
        super().cost()
        return f' Cost of this boat is {self.cost}'

    def colour(self, colour):
        super().colour()
        return f'Colour of this boat is {self.colour}'

    def mark(self, mark):
        super().mark()
        return f'Mark of this boat is {self.mark}'


m = Moto(1000, "red", "bmv")
print(str(m))
m.speed(200)
a = Auto(15000, "blue", "Volvo")
print(str(a))
a.type("hetchback")
a.seats(4)
b = Boat(30000, "white", "bavaria")
print(str(b))
b.type("motor boat")
b.speed(70)

