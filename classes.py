class Details:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} {self.age}")

class Hostel(Details):
    def greet(self):
        print(f"Hi, I'm {self.name}, a hostellite with fees of 85k")

class Dayscholar(Details):
    def fees(self):
        print(f"I'm {self.name}, a day scholar with varying fees")

# Creating instances
pra = Details("Praneeth", 25)
pra.greet()


hostelite = Hostel("Praneeth", 20)
hostelite.greet()
#hostelite.fees()

day_scholar = Dayscholar("Day Scholar", 18)
#day_scholar.greet()
day_scholar.fees()
