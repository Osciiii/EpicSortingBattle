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
    for i in range(len(items)):
        for j in range(i):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    return items


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
