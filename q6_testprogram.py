# I modified the file for analysis purpose, the original file u can still find if you scroll down
import random
import time
import matplotlib.pyplot as plt
from q6_sort import Vehicle, selectionSort, bubbleSort, mergeSort

# Create vehicle objects with random data
def createRandomVehicles(numVehicles):
    manufacturers = ['Toyota', 'Ford', 'Volkswagen', 'BMW', 'Honda']
    models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model F'] # Each manufacturer has their own model so idk lol, I'd say version is better but oh well
    types = ['Sedan', 'SUV', 'Truck', 'Coupe', 'Sedan']
    vehicles = []

    for _ in range(numVehicles):
        manufacturer = random.choice(manufacturers)
        model = random.choice(models)
        type_ = random.choice(types)
        cost = random.randint(10000, 100000)  
        mileage = random.randint(0, 100000) 

        vehicle = Vehicle(manufacturer, model, type_, cost, mileage)
        vehicles.append(vehicle)

    return vehicles

# Measure execution time 
def measureTime(sortFunction, lst):
    startTime = time.time()  
    sortFunction(lst)           
    endTime = time.time() 
    return endTime - startTime 


# Testing 
def testing():
    sizes = [10, 100, 1000, 5000, 10000]  
    selectionSortTime = []
    bubbleSortTime = []
    mergeSortTime = []

    for size in sizes:
        vehicles = createRandomVehicles(size)
        
        # Measure time for each sorting algorithm
        selectionSortTime.append(measureTime(selectionSort, vehicles[:]))
        bubbleSortTime.append(measureTime(bubbleSort, vehicles[:]))
        mergeSortTime.append(measureTime(mergeSort, vehicles[:]))

    # Print
    for size, selection, bubble, merge in zip(sizes, selectionSortTime, bubbleSortTime, mergeSortTime):
        print(f"List size: {size} - Selection Sort: {selection:.6f}s, Bubble Sort: {bubble:.6f}s, Merge Sort: {merge:.6f}s")
    
    # Pllot it
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, selectionSortTime, label="Selection Sort", marker='o')
    plt.plot(sizes, bubbleSortTime, label="Bubble Sort", marker='o')
    plt.plot(sizes, mergeSortTime, label="Merge Sort", marker='o')

    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()

    plt.show()

if __name__ == "__main__":
    testing()

"""
import random
from q6_sort import Vehicle, selectionSort, bubbleSort, mergeSort

# Create vehicle objects with random data
def createRandomVehicles(numVehicles):
    manufacturers = ['Toyota', 'Ford', 'Volkswagen', 'BMW', 'Honda']
    models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model F'] # Each manufacturer has their own model so idk lol, I'd say version is better but oh well
    types = ['Sedan', 'SUV', 'Truck', 'Coupe', 'Sedan']
    vehicles = []

    for _ in range(numVehicles):
        manufacturer = random.choice(manufacturers)
        model = random.choice(models)
        type_ = random.choice(types)
        cost = random.randint(10000, 100000)  
        mileage = random.randint(0, 100000) 

        vehicle = Vehicle(manufacturer, model, type_, cost, mileage)
        vehicles.append(vehicle)

    return vehicles


# Test the sorting algorithms 
def testing():
  
    vehicles = createRandomVehicles(10)

    print("Original list of vehicles:")
    for vehicle in vehicles:
        print(vehicle)

    # Sort using selection sort
    print("\nSorted by Selection Sort (by cost):")
    sortedVehicles = selectionSort(vehicles[:])  
    for vehicle in sortedVehicles:
        print(vehicle)

    # Sort using bubble sort
    print("\nSorted by Bubble Sort (by cost):")
    sortedVehicles = bubbleSort(vehicles[:])  
    for vehicle in sortedVehicles:
        print(vehicle)

    # Sort using merge sort
    print("\nSorted by Merge Sort (by cost):")
    sortedVehicles = mergeSort(vehicles[:])  
    for vehicle in sortedVehicles:
        print(vehicle)



if __name__ == "__main__":
    testing()
"""