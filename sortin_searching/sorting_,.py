def Bubble(list_: list):
    for j in range(len(list_)):
        for i in range(len(list_) - 1):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]

    return list_

def Bubble(list_: list):
    swapped = True
    for j in range(len(list_)):
        if swapped:
            lis = list_.copy()
            for i in range(len(list_) - 1):
                if list_[i] > list_[i + 1]:
                    list_[i], list_[i + 1] = list_[i + 1], list_[i]

            if lis == list_:
                swapped = False
                
        else:
            return list_ 

def Insertion(list_: list):
    for i in range(1, len(list_)):
        key = list_[i]
        j = i -1

        while key < list_[j] and j >= 0:
            list_[j + 1], list_[j] = list_[j], key
            j -= 1

    return list_ 

def Selection(list_: list):
    for i in range(len(list_)):
        min_index = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[min_index]:
                min_index = j

        if min_index != i:
            list_[min_index], list_[i] = list_[i], list_[min_index]

    return list_

def Merge(list_: list):
    if len(list_) > 1:
        mid = int(len(list_) / 2)
        Left = list_[:mid]
        Right = list_[mid:]
        Merge(Left)
        Merge(Right)

        i = 0
        j = 0
        k = 0
        while i < len(Left) and j < len(Right):
            if Left[i] <= Right[j]:
                list_[k] = Left[i]
                i += 1
            else:
                list_[k] = Right[j]
                j += 1

            k += 1

        while i < len(Left):
            list_[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            list_[k] = Right[j]
            j += 1
            k += 1

    return list_

def Quick(list_: list):
    if len(list_) > 1:
        index = len(list_) - 1
        j = 0
        for i in range(len(list_)):
            if list_[i] < list_[index]:
                list_[j], list_[i] = list_[i], list_[j]
                j += 1
            
        list_[j], list_[index] = list_[index], list_[j]

        piv = j
        left = Quick(list_[:piv])
        right = Quick(list_[piv:])

        return left + right

    return list_

print("Bubble sort:", Bubble([2, 1, 5, 9, 0, 3, -9, -2]))

print("Insertion sort:", Insertion([2, 1, 5, 9, 0, 3, -9, -2]))

print("Selection sort:", Selection([2, 1, 5, 9, 0, 3, -9, -2]))

print("Merge sort", Merge([2, 1, 5, 9, 0, 3, -9, -2]))

print("Quick sort:", Quick([2, 1, 5, 9, 0, 3, -9, -2]))