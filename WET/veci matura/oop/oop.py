class Person:
    def __init__(self, name, age):#konstruktor , self se váže ke classe
        self.name = name
        self.age = age
        self.alive = True

    def greeting(self):
        print(f"Hello, I'm  {self.name}")

    def parting(self):# funkci se říká metoda pokud je uvnitř classy
        print(f"Bye, {self.name} is out!")

fridolin = Person("Fridolín", 102)
fridolin.greeting()
fridolin.parting()

class Student(Person):
    def __init__(self, name, age, class_name):
        super().__init__(name, age)
        self.class_name = class_name

petr = Student("Petr",6,"1.B")
petr.greeting()

print(petr.alive)