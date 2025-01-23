def decorate(func):

    def wrapper(numbers):
        if not numbers:
                print("No number to process")
                return func(numbers)
        
        count = len(numbers)
        average = sum(numbers) / count
        maxium = max(numbers)

        print(f"The numbers read: {numbers}")
        print(f"The count of numbers read: {count}")    
        print(f"The average of the numbers: {average:.2f}")
        print(f"The maxium of the numbers: {int(maxium)}")
        print(f"-" * 40)

        return func(numbers)
    return wrapper

def processLine(numbers):
     return numbers

processLine = decorate(processLine)

# try is better than if else in this case cuz it will automatically catch any errors instead of having to detail to a specific error like if else
def printStats(t):
    try:
        with open(t, 'r') as file:
            for line in file:
                # Makes sure that it goes thru every line even if the first one has non-numeric value
                try:
                    numbers = [int(num) for num in line.split()] # Split the line into individual piece seperated based on space then convert into int and store in numbers
                    processLine(numbers) 
                except ValueError:
                    print("Error: Ensure the file contains only valid numeric values")
                    print(f"-" * 40)
                    continue

    except FileNotFoundError:
        print(f"Error: The file '{t}' was not found")


printStats("q4.txt")