import random, copy

def insertionSort(items):
    for i in range(1, len(items)): # Gå over listen ved at starte ved det andet element
        key = items[i] # Lagre det nuværende element som key
        q = i-1
        while q >= 0 and key < items[q]: # Flyt elementer større en key en position frem
            items[q+1] = items[q] # Flytter elementer til højre
            q -= 1
        items[q+1] = key # Indsætter key i den korrekte position
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
    if len(items) > 1:
        # Deler listen i to forskellige lister den venstre og højre liste
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        # Kalder på begge halvdele af listen
        mergeSort(left)
        mergeSort(right)

        # De two variabler til de to halve af listen
        i = 0
        j = 0

        # Variablen for hovedlisten
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # Hvis det venstre element er større placer det i hovedlisten
                items[k] = left[i]
                # Flytter variablen fremad
                i += 1
            else:
                # Hvis det højre element er større placer det i hovedlisten
                items[k] = right[j]
                j += 1
            # Flytter til det næsten slot
            k += 1

        # Kopiere resten af elementerne fra den venstre liste hvis der er nogen
        while i < len(left):
            items[k] = left[i]
            i += 1
            k += 1

        # Kopiere resten af elementerne fra den højre liste hvis der er nogen
        while j < len(right):
            items[k] = right[j]
            j += 1
            k += 1
    return items # retunere den sorterede liste



if __name__ == '__main__':
    l = list(range(0, 10))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)

        ## Kald den funktion, du vil teste
        ls = insertionSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)


