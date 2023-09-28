import sys

class Student:
    students = []

    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        if self.felhantering_personnummer(personnummer):
            self.personnummer = personnummer
            if len(self.__class__.students) < 3:
                self.__class__.students.append(self)
                print("Objektet skapat!")
            else:
                sys.exit()
        else:
            print("Personnummret får endast bestå av siffror!")
        
    def __str__(self):
        return "Namn:"+ self.förnamn  + self.efternamn + "Personnummer:" + self.personnummer
    
    def felhantering_personnummer(self, personnummer):
        return personnummer.isdigit()        
    
students = []
while len(Student.students) < 3:
    förnamn = input("Vad är studentens förnamn?")
    efternamn = input("Vad är studentens efternamn?")
    personnummer = input("Vad är studentens personnummer?")
    student = Student(förnamn,efternamn, personnummer)
    
print("Här är alla sparade objekt:")
for student in Student.students:
    print(student)
    




