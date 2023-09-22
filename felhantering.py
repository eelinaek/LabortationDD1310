"""Elina Ek, Nellie Rosén, Helena Salwén
2023-09-22
DD1013 Laboration 3, modul"""            

def inmatning_flyttal(inmatning):
    """Inmatning och felhantering av flyttal.
    In: Flyttal inmatat från användaren.
    Ut: Felhanterade flyttal till beräkningar."""
    while True:
        try:
            inmatning = float(input(inmatning))
            return inmatning
        except ValueError:
            print("Det där var inget flyttal, försök igen!")

def inmatning_heltal(inmatning):
    """Inmatning och felhantering av heltal.
    In: Heltal inmatat från användaren. 
    Ut: Felhanterade heltal till beräkningar. """
    while True:
        try:
            inmatning = int(input(inmatning))
            return inmatning
        except ValueError:
            print("Det där var inget heltal, försök igen!")
    