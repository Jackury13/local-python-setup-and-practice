class Car:
    def __init__(self, name):  
        print('Hello')
        self.name = name

    def start(self):
        print("Vroom!")

    def talk(self, driver):
        print(f"greetings, {driver}. i am {self.name}.")

my_car = Car('Tesla')
print(my_car.name)



