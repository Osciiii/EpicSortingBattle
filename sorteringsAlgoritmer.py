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
    for i in range(len(items)):
        for j in range(i):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    return items


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
