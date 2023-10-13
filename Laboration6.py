"""Nellie Rosén, Elina Ek, Helena Salwén
2023-10-13
DD1310 Laboration 6"""

class Student:
    """Klass som representerar student med förnamn, efternamn och personnummer."""
    def __init__(self, personnummer, efternamn, förnamn):
        """Skapar en student med data från filen"""
        self.personnummer = personnummer
        self.efternamn = efternamn
        self.förnamn = förnamn

    def __str__(self):
        """Skriver ut studentens information."""
        return "Namn: "+ self.förnamn + " " + self.efternamn+ " " + "Personnummer: " + self.personnummer
    
class Skola:
    """Klass som sparar information om studenterna."""
    def __init__(self):
        """Skapar lista för att spara information."""
        self.studenter = []

    def addera_ny_student(self, student):
        """Lägger till en ny studentent i den sparade listan av studenter."""
        self.studenter.append(student)

    def skriv_ut_studenter(self):
        """Skriver ut listan av studenter."""
        print("Dessa studenter är skrivna på KTH:")
        for student in self.studenter:
            print(student)    

def läs_studentdata_från_fil(filnamn):
    """Öppnar och läser filen, delar upp data till rätt kategorier 
    och lägger in datan i listan. Felhanterar om den angivna filen inte
    finns och ger användaren möjlighet att skriva en ny."""
    skola = Skola()
    while True:
        try:
            with open(filnamn, 'r', encoding='utf-8' ) as fil:
                rad = fil.readline()
                while rad:
                    personnummer = rad.strip()
                    efternamn = fil.readline().strip()
                    förnamn = fil.readline().strip()
                    student = Student(personnummer, efternamn, förnamn)
                    skola.addera_ny_student(student)
                    rad = fil.readline()
                return skola
        except FileNotFoundError:
            print("Filen hittades inte!")
            filnamn = input("Skriv filen igen, eller prova en annan:")
    
def huvudprogram():
    """Frågar användaren om vilken fil som ska användas
    och kontrollerar att data finns i filen."""
    filnamn = input("Ange filnamnet med studentdata: ")
    skola = läs_studentdata_från_fil(filnamn)
    if skola.studenter:
        skola.skriv_ut_studenter()
    else:
        print("Ingen studentdata hittades i filen.")
huvudprogram()