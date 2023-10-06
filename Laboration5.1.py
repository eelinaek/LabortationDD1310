"""Nellie Rosén, Elina Ek, Helena Salwén
2023-10-06
DD1310 Laboration 5"""

class Student:
    """Klass som representerar student med förnamn, efternamn och personnummer"""
    def __init__(self, förnamn, efternamn, personnummer):
        """Skapar en ny student med förnamn, efternamn och personnummer från användare."""
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer
        
    def __str__(self):
        """Skriver ut en sträng för namn och personnummer för studenten."""
        return "Namn: "+ self.förnamn + " " + self.efternamn + " " + "Personnummer: " + self.personnummer

class Skola:
    """Klass som sparar information om studenter, men information från student."""
    def __init__(self):
        """Skapar lista för att spara information"""
        self.studenter = []

    def addera_ny_student(self, student):
        """Lägger in ny student i den sparade listan av studenter."""
        self.studenter.append(student)


def inmatning_av_ny_student():
    """Inmatning av data för studenter.
    In:Namn och personnummer inmatat av student
    Ut: Skapar student med hjälp av klassen Student
    Returnerar felmeddelande om datan inte är korrekt."""
    while True:
        förnamn = input("Vad är studentens förnamn? ")
        efternamn = input("Vad är studentens efternamn? ")
        if förnamn.isalpha and efternamn.isalpha ():
            return Student (förnamn,efternamn, personnummer)
        else:
            print("Namn får endast innehålla bokstäver, försök igen!")
        personnummer = input("Vad är studentens personnummer? ")
        if personnummer.isdigit():
            return Student(förnamn, efternamn, personnummer)
        else:
            print("Personnumret får bara innehålla siffror, försök igen!")

def huvudprogram():
    """Ger information till användaren vad som ska göras. 
    In: Godkända inmatningar
    Ut: Lägger in data i listan och avslutar programmet, skriver ut lista, när tre studenter är inmatade"""
    skola = Skola()
    while len(skola.studenter) < 3:
        print("Information om studenten: ")
        student = inmatning_av_ny_student()
        skola.addera_ny_student(student)
        print("Studenten är tillagd!")

    print("Här är alla studenter på KTH:")
    for student in skola.studenter:
        print(student)

huvudprogram()
