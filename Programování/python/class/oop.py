class Student():
    def __init__(self ,name ,school ,colour ):
        self.name = name
        self.school = school
        self.fav_colour = colour
    def speak(self,pozdrav):
        print(f"{pozdrav}moje oblíbená barva je {self.fav_colour}")

class Zak(Student):
    def __init__(self ,name ,school ,colour ):
        super().__init__(name ,school ,colour )

kubko = Student("Kubko", "Třebešín", "green")

print(kubko.fav_colour)
kubko.speak("Ahoj ")

ema = Student("Ema", "Užlabina", "blue")
ema.speak("Čau ")

ida = Zak("Ida","Skola","blue" )
ida.speak("Achoj ")