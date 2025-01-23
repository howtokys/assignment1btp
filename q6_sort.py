import random

class Vehicle:
    def __init__(self, manufacturer, model, type_, cost, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.type_ = type_
        self.cost = cost
        self.mileage = mileage

    def __repr__(self):
        return f"Vehicle(manufacturer = '{self.manufacturer}', model = '{self.model}', type_ = '{self.type_}', cost = {self.cost}, mileage = {self.mileage})"
    
    # Less than
    def __lt__(self, other):
        return self.cost < other.cost
    
    # Greater than
    def __gt__(self, other):
        return self.cost > other.cost
    
    # Equal
    def __eq__(self, value):
        return self.cost == value.cost


# Sorting algorithms
def selectionSort(lst):
    n = len(lst)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if lst[j].cost < lst[minIndex].cost:
                minIndex = j
        lst[i], lst[minIndex] = lst[minIndex], lst[i]
    return lst


def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j].cost > lst[j+1].cost:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    
    middle = len(lst) // 2
    left = mergeSort(lst[:middle])  
    right = mergeSort(lst[middle:])
    
    return merge(left, right)

# Merge helper function

def merge(left, right):
    sortedList = []
    while left and right:
        if left[0].cost < right[0].cost:
            sortedList.append(left.pop(0))
        else:
            sortedList.append(right.pop(0))
    
    # If one of the lists is not empty, add the remaining elements
    sortedList.extend(left)
    sortedList.extend(right)
    return sortedList
