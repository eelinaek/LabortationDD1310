"""Elina Ek, Nellie Rosén, Helena Salwén
2023-09-22
DD1013 Laboration 3, huvudprogram"""

import felhantering

def beräkna_aritmetrisk_summa(första_element, antal_termer, differens):
    """Beräknar den aritmetriska summan.
    In: Invärden för den aritmetiska summan från användaren i huvudprogrammet.
    Ut: Den beräknade aritmetiska summan."""
    aritmetrisk_summa = antal_termer * ((första_element + (första_element + differens * (antal_termer - 1))) / 2)
    return aritmetrisk_summa

def beräkna_geometrisk_summa(första_element, antal_termer, kvot):
    """Beräknar den geometriska summan.
    In: Invärden från den geometriska summan från användaren i huvudprogrammet.
    Ut: Den beräknade aritmetiska summan."""
    geometrisk_summa = första_element*(((kvot**antal_termer) - 1)/(kvot - 1))
    return geometrisk_summa

def huvudprogram():
    """Tar all input till talföljderna från användaren och jämför summorna.
    In:Invärden från användaren och summan hos talföljderna från tidigare funktioner.
    Ut:Jämförelse mellan summorna av de olika talföljderna."""
    print("Data för den aritmetriska summan:") 
    """Tar emot data för den aritmetiska summan."""
    första_element_a1 = felhantering.inmatning_flyttal("Skriv in startvärdet: ")
    differens = felhantering.inmatning_flyttal("Skriv in differensen: ")
    
    print("Data för den geometriska summan:")
    """Tar emot data för den geometriska summan och säkerställer att den är definerad."""
    första_element_g1 = felhantering.inmatning_flyttal("Skriv in startvärdet: ")
    while True:
        kvot = felhantering.inmatning_flyttal("Skriv in kvoten: ")
        if kvot == 1:
            print("Då kvot = 1 blir nämnaren odefinierad och summan kan ej beräknas.")
            continue
        else:
            break

    print("Antal termer i summorna:")
    """Tar emot data för antal element i talföljderna och säkerställer att den är definerad."""
    while True:
        antal_termer = felhantering.inmatning_heltal("Skriv in antal termer i följden: ")
        if antal_termer <= 0:
            print ("Antal termer måste vara större än noll. Försök igen!")
            continue
        else:
            break
        
    """Jämför den aritmetriska och geometriska summan och skriver ut vilken som är störst"""
    aritmetrisk_summa = beräkna_aritmetrisk_summa(första_element_a1, antal_termer, differens)
    geometrisk_summa = beräkna_geometrisk_summa(första_element_g1, antal_termer, kvot)
    if aritmetrisk_summa < geometrisk_summa:
        print("Den geometriska summan är störst.")
    elif geometrisk_summa < aritmetrisk_summa:
        print("Den aritmetriska summan är störst.")
    else:
        print("De två summorna är lika stora.")
huvudprogram()
