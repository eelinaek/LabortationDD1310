"""Elina Ek 
2023-11-29
DD1310 Projektarebete Telefonregister"""
class Person:
    """Klass som representerar person med förnamn, efternamn, telefonnummer, email och adress"""
    def __init__(self, efternamn, förnamn, telefonnummer, email, adress):
        self.efternamn = efternamn
        self.förnamn = förnamn
        self.telefonnummer = telefonnummer
        self.email = email
        self.adress = adress

    def __str__(self):
        """Skriver ut information om personer när de söks efter"""
        return (self.efternamn.ljust(14))+(self.förnamn.ljust(15))+(self.telefonnummer.ljust(17))+(self.email.ljust(35))+(self.adress.ljust(25))

    def __lt__(self, other):
        """Sorterar registret med personer med hjälp av efternamn """
        return self.efternamn < other.efternamn

class Register:
    """Klass som sparar information om personer"""
    def __init__(self):
        """Skapar lista med information av personer"""
        self.personer = []

    def lägg_till_person(self, person):
        """Lägger till personer i lista"""
        self.personer.append(person)
   
    def sök_efternamn(self, efternamn):
        """Söker efternamn i listan med personer"""
        hittade_personer = [person for person in self.personer if person.efternamn.lower() == efternamn.lower()]
        return hittade_personer

    def sök_förnamn(self, förnamn):
        """Söker förnamn i listan med personer"""
        hittade_personer = [person for person in self.personer if person.förnamn.lower() == förnamn.lower()]
        return hittade_personer

    def sök_telefonnummer(self, telefonnummer):
        """Söker telefonnummer i listan med personer"""
        hittade_personer = [person for person in self.personer if person.telefonnummer == telefonnummer]
        return hittade_personer

    def sök_email(self, email):
        """Söker email i listan med personer"""
        hittade_personer = [person for person in self.personer if person.email.lower() == email.lower()]
        return hittade_personer

    def sök_adress(self, adress):
        """Söker adress i listan med personer"""
        hittade_personer = [person for person in self.personer if person.adress.lower() == adress.lower()]
        return hittade_personer

    def radera_person(self, person):
        """Raderar person från listan med personer"""
        self.personer.remove(person)

    def ändra_uppgifter(self, person, nytt_telefonnummer, ny_email, ny_adress):
        """Ändrar person i listan med personer"""
        person.telefonnummer = nytt_telefonnummer
        person.email = ny_email
        person.adress = ny_adress

    def visa_register(self):
        """Skriver ut register, i början av programmet och när det önskas sorterat."""
        print("Förnamn".ljust(14)+"Efternamn".ljust(15)+"Telefonnummer".ljust(17)+"Email".ljust(35)+"Adress".ljust(25))
        print("------------------------------------------------------------------------------------------------")
        for person in self.personer:
            print((person.efternamn.ljust(14))+(person.förnamn.ljust(15))+(person.telefonnummer.ljust(17))+(person.email.ljust(35))+(person.adress.ljust(25)))
        

def läs_register():
    """INPUT: Data från fil med personuppgifter
    OUTPUT: Sorterad data för att skapa person och bilda en lista
    Felhanterad om önskad fil inte finns."""
    register = Register()
    try:
        with open('register.txt', 'r', encoding='utf-8') as fil:
            for rad in fil:
                rad = rad.strip()
                personlista = rad.split(";")

                
                if len(personlista) == 5:
                    efternamn = personlista[0]
                    förnamn = personlista[1]
                    telefonnummer = personlista[2]
                    email = personlista[3]
                    adress = personlista[4]

                    person = Person(efternamn, förnamn, telefonnummer, email, adress)
                    register.lägg_till_person(person)
                else:
                    print("Ogiltig rad i filen: ", rad)
        return register
    except FileNotFoundError:
        print("Filen hittades inte!")
        return None


def spara_register(register):
    """INPUT: Ändrad och tillagd information om personer
    OUTPUT: Ändrade uppgifter till fil"""
    with open ('register.txt', 'w', encoding='utf-8') as fil:
        for person in register.personer:
            fil.write(person.efternamn + ";" + person.förnamn + ";" + person.telefonnummer + ";" + person.email + ";" + person.adress + "\n")

def felhantering_namn(inmatning):
    """INPUT: Användares inmatning av för- och efternamn
    OUTPUT:Felhanterad inmatning, kontroll av bokstäver."""
    while True: 
        namn = input(inmatning)
        if namn.isalpha():
            return namn
        else:
            print("Namn får endast bestå av bokstäver, försök igen!")

def felhantering_telefonnummer(inmatning):
    """INPUT: Användares inmatning av telefonnummer
    OUTPUT: Felhanterad inmatning, kontroll av siffror och längd."""
    while True:
        telefonnummer = input(inmatning)
        if telefonnummer.isdigit():  
            if len(telefonnummer) == 10:
                return telefonnummer
            else:
                print("Telefonnummer måste vara 10 siffror långt!")
        else:
            print("Telefonnummer får endast bestå av siffror!")

def felhantering_email(inmatning):
    """INPUT: Användarens inmatning av email
    OUTPUT: Felhanterad inmatning, kontroll av format."""
    while True:
        email = input(inmatning)
        if "@" in email and "." in email:
            return email
        else:
            print("Ogiltigt format på email, försök igen!")
            
def felhantering_adress(inmatning):
    """INPUT: Användarens inmatning av adress
    OUTPUT: Felhanterad inmatning, kontroll av format och siffra."""
    while True:
        adress = input(inmatning)
        delar= adress.split()
        if len(delar) >= 2 and delar[-1].isdigit():
            return adress
        else:
            print("Adress skrivet i ogiltigt format, försök igen!")
    
def sök_efternamn(register):
    """INPUT: Efternamn från användare som felhanteras i angiven funktion
    OUTPUT: Hittade personer som matchar från lista av register"""
    efternamn = felhantering_namn("Vilket efternamn söker du efter?")
    hittade_personer = register.sök_efternamn(efternamn)
    if hittade_personer:
        for person in hittade_personer:
            print(person)
    else:
        print("Ingen person matchade din sökning")

def sök_telefonnummer(register):
    """INPUT:Telefonnummer från användare som felhanterats i angiven funktion
    OUTPUT: Hittade personer som matchar från lista med register"""
    telefonnummer = felhantering_telefonnummer("Vilket telefonnummer söker du efter?")
    hittade_personer = register.sök_telefonnummer(telefonnummer)
    if hittade_personer:
        for person in hittade_personer:
            print(person)
    else: 
        print("Ingen person matchade din sökning")

def sök_email(register):
    """INPUT: Email från användare som felhanteras i given funktion
    OUTPUT: Hittade personer som matchar i lista av register"""
    email = felhantering_email("Vilken email söker du efter?")
    hittade_personer = register.sök_email(email)
    if hittade_personer:
        for person in hittade_personer:
            print(person)

def lägg_till_person(register):
    """INPUT: Information om ny kontakt från användare 
    OUTPUT: Ny kontakt i listan med register"""
    print("Fyll i information om din nya kontakt nedan!")
    efternamn = felhantering_namn("Ange efternamn:")
    förnamn = felhantering_namn("Ange förnamn:")
    telefonnummer = felhantering_telefonnummer("Ange telefonnummer:")
    email = felhantering_email("Ange email:")
    adress = felhantering_adress("Ange adress:")  
    ny_person = Person(efternamn, förnamn, telefonnummer, email, adress)
    register.lägg_till_person(ny_person)
    print("Personen har lagts till i telefonregistret!")       
    
def ta_bort_person(register):
    """Tar bort person från registret. 
    INPUT: Användarens val om person som ska raderas och bekräftelse.
    OUTPUT: Tar bort person från listan i register."""
    efternamn = felhantering_namn("Vilket efternamn har personen du vill ta bort?")
    hittade_personer = register.sök_efternamn(efternamn)

    if hittade_personer:
        print("Dessa personer matchar din sökning:")
        for person in hittade_personer:
            print(person)

        val = felhantering_namn("Skriv förnamn på personen du vill ta bort:")

        person_att_ta_bort = None
        for person in hittade_personer:
            if person.förnamn.lower() == val.lower():
                person_att_ta_bort = person
                break

        if person_att_ta_bort:
            bekräftelse = input("Vill du verkligen ta bort" + (person_att_ta_bort.efternamn) +" "+(person_att_ta_bort.förnamn)+"? (ja/nej): ").lower()
            
            if bekräftelse == "ja":
                register.radera_person(person_att_ta_bort)
                print((person_att_ta_bort.efternamn)+" "+(person_att_ta_bort.förnamn)+" "+ "har tagits bort från registret.")
            else:
                print("Åtgärd avbruten.")
        else:
            print("Ingen person hittades med det angivna namnet.")
    else:
        print("Ingen person hittades.")

def ändra_telefonnummer(person):
    """INPUT: Användares inmatning om nytt telefonnummer
    OUTPUT: Ändrat telefonnummer och information om person"""
    nytt_telefonnummer = felhantering_telefonnummer("Ange nytt telefonnummer:")
    person.telefonnummer = nytt_telefonnummer

def ändra_email(person):
    """INPUT: Användares inmatning om ny email
    OUTPUT: Ändrad email och information om person"""
    ny_email = felhantering_email("Ange ny email:")
    person.email = ny_email

def ändra_adress(person):
    """INPUT: Användares inmatning om ny adress
    OUTPUT: Ändrad adress och information om person"""
    ny_adress = felhantering_adress("Ange ny adress:")
    person.adress = ny_adress

def ändra_uppgifter(register):
    """INPUT: Användares inmatning om person som ska ändras och vad som ska ändras
    OUTPUT: Information skickas till berörd funktion"""
    efternamn = felhantering_namn("Ange efternamnet för personen du vill ändra uppgifter för: ")
    hittade_personer = register.sök_efternamn(efternamn)

    if hittade_personer:
        print("Dessa personer matchar din sökning:")
        for person in hittade_personer:
            print(person)
            
        förnamn = felhantering_namn("Ange förnamnet för personen du vill ändra uppgifter för: ")

        hittad_person = None
        for person in hittade_personer:
            if person.förnamn.lower() == förnamn.lower():
                hittad_person = person
                break

        if hittad_person:
            print("Vad vill du ändra för" +(person.förnamn)+ " " +(person.efternamn))
            print("Telefonnummer?")
            print("Email?")
            print("Adress?")

            val = input("Ange ditt val: ")

            if val == "Telefonnummer":
                ändra_telefonnummer(hittad_person)
            elif val == "Email":
                ändra_email(hittad_person)
            elif val == "Adress":
                ändra_adress(hittad_person)
            else:
                print("Ogiltigt val.")
                val = input("Försök igen")

            print("Uppgifterna för" +" "+(hittad_person.förnamn) +" "+ (hittad_person.efternamn)+" "+ "har ändrats.")
        else:
            print("Ingen person hittades med det angivna förnamnet.")
    else:
        print("Ingen person hittades.")

    

def sortera_och_skriv_ut(register):
    """Sorterar registret enligt efternamn"""
    register.personer.sort()
    register.visa_register()

def avsluta_programmet(register):
    """Avslutar programmet och sparar ändringar i filen"""
    spara_register(register)
    print("Programmet avslutas.")

def meny():
    """Meny för användare, vad som är möjligt att göra i programmet"""
    print("\nVad vill du göra?")
    print("1. Sök efter efternamn")
    print("2. Sök efter telefonnummer")
    print("3. Sök efter email")
    print("4. Lägg till ny person")
    print("5. Ta bort person")
    print("6. Ändra uppgifter för person")
    print("7. Sortera och skriv ut registret")
    print("8. Avsluta programmet")

def menyval(val, register):
    """Användares menyval skickas till berörd funktion."""
    menyval = {
        "1": sök_efternamn,
        "2": sök_telefonnummer,
        "3": sök_email,
        "4": lägg_till_person,
        "5": ta_bort_person,
        "6": ändra_uppgifter,
        "7": sortera_och_skriv_ut,
        "8": avsluta_programmet
    }

    if val in menyval:
        menyval[val](register)
    else:
        print("Ogiltigt val. Försök igen.")

def använda_meny():
    """Startar programmet. Skriver ut register och användaren får välja vilket menyval den vill göra."""
    register = läs_register()
    print("TELEFONREGISTER")
    register.visa_register()
    if register and register.personer:
        while True:
            meny()
            val = input("Ange ditt val (1-8): ")
            menyval(val, register)

använda_meny()