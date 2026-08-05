def Linear(list_: list, item):
    found = False
    index = 0

    while len(list1) > index and not found:
        if list_[index] == item:
            found = True

        else:
            index += 1

    return found

        


def Binary(list_: list, item):
    found = False
    start = 0
    end = len(list_) - 1
    
    while not found and start <= end:
        mid = (start + end) // 2
        if list_[mid] == item:
            found = True

        elif item > list_[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return found

list1 = [12, 0, 8, 9, 67, 5, 45, 20]

print(Linear(list1, 89))

list1.sort()

print(Binary(list1, 10))