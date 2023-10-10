import random, copy

def insertionSort(items):
    for i in range(1, len(items)):
        key = items[i]
        q = i-1
        while q >= 0 and key < items[q]:
            items[q+1] = items[q]
            q -= 1
        items[q+1] = key
    return items



def bubbleSort(items):
    # Dette er en funksjonsdefinisjon for en Bubble Sort-algoritme.
    # Bubble Sort er en enkel sorteringsalgoritme som sammenligner hvert par av tilstøtende elementer og bytter dem hvis de er i feil rekkefølge.

    for i in range(len(items)):
        # Dette er en ydre løkke som går gennem alle elementene i listen 'items'.

        for j in range(i):
            # Dette er en indre løkke som går gennem elementene fra starten af listen til 'i-1'.
            # Denne løkke bruges til at sammenligne og bytte elementer.
            if items[j] > items[j+1]:
                # Dette er en betinget sætning som sammenligner to elementer.
                # Hvis elementet på position 'j' er større en elementet på position 'j+1', byttes de to elementene.
                temp = items[j]
                # Opretter en midlertidig variabel 'temp' og lagrer værdien af 'items[j]' i den.
                items[j] = items[j+1]
                # Sætter værdien af 'items[j]' til at være lig værdien af 'items[j+1]'.
                items[j+1] = temp
                # Sætter værdien af 'items[j+1]' til at være lig værdien som tidligere blev lagret i 'temp'.
    return items
    # Returnerer den sorterede liste 'items'.


def mergeSort(items):


if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)

        ## Kald den funktion, du vil teste
        ls = bubbleSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)


