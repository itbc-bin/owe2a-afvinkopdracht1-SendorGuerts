# Naam:
# Datum:
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    try:
        bestand = input("vul hier de naam van het fasta bestand in")   # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
        """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """

        headers, seqs = lees_inhoud(bestand)

        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print(headers[i])
                seq = seqs[i]
                print("sequentie is dna?", is_dna(seq))
                print(knipt(seq))
    except FileNotFoundError:
        if ".fa" not in bestand:
            print("verkeerde format")
        else:
            print("Voeg een bestaand bestand in")

    # schrijf hier de rest van de code nodig om de aanroepen te doen
def lees_inhoud(bestand):
    bestand = open(bestand)
    headers = []
    seqs = []
    seq = ''
    for line in bestand:
        line = line.strip()

        if ">" in line:
            headers.append(line)
            if len(seq) > 0:
                seqs.append(seq)
                seq = ""
        else:
            seq += line
    seqs.append(seq)
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """

    return headers, seqs


def is_dna(seq):
    # A,T,C,G aantal berekenen en defineren
    A = seq.count('A')
    T = seq.count('T')
    C = seq.count('C')
    G = seq.count('G')


    # hoeveelheid atcg berekenen en defineren
    Aantalatcg = A + T + C + G



    # kijken of het aantal atcg gelijk is aan de lengte van de sequentie, zo niet print nee
    if Aantalatcg == len(seq):
        return True
    else:
        return False

    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """


def knipt(seq):
    enzymen = []

    bestand = open("enzymen.txt")

    for line in bestand:
        combi = line.split()
        enzymen.append(combi)

    for plek in enzymen:
        plek[1] = plek[1].replace('^', '')
    for plek in enzymen:
        if plek[1] in seq:
            #pos = seq.index(plek[1])
            #A = pos * " " + plek[1]
            #print(seq)
            #print(A)
            #print("match:", plek[0], plek[1])
            print("knipt", enzymen[0])
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken
    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """


main()
