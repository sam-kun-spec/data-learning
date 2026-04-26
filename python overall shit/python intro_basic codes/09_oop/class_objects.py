# class is a blueprint or a temlplate for creating an object (kind a placeholder something)
class details:
    name = "sam kun"
    age = 19
    def info(self):
        print(f"{self.name} is {self.age} years old")

a = details()
a.name = "ku kun"
a.age = 18

b = details()
b.name = "nah nha"
b.age = 23

print(a.name,"is",a.age,"years old")
print(b.name,"is",b.age,"years old")
a.info()

# another example: a simple Car class
class Car:
    brand = "Toyota"
    speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} is going at {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        print(f"{self.brand} slowed down to {self.speed} km/h")

my_car = Car()
my_car.brand = "Honda"
my_car.accelerate()
my_car.accelerate()
my_car.brake()