import matplotlib.pyplot as plt
def graphSnowfall(t):
    snowfallData = []
    with open(t, 'r') as file: # r mean read mode
        for line in file:
            if line.strip(): # line.strip removes spaces and newline
                snowfallData.append(int(line.strip())) #int because the number is not actually a number, more like a string so it can convert into int
    print(snowfallData)

    # Create the range 
    # 0 cuz counting starts at 0 duh
    ranges = {
        '0-10 cm': 0,
        '11-20 cm': 0,
        '21-30 cm': 0,
        '31-40 cm': 0,
        '41-50 cm': 0 
    }

    # Count
    for i in snowfallData:
        if 0 <= i <= 10:
            ranges['0-10 cm'] += 1
        elif 11 <= i <= 20:
            ranges['11-20 cm'] += 1
        elif 21 <= i <= 30:
            ranges['21-30 cm'] += 1
        elif 31 <= i <= 40:
            ranges['31-40 cm'] += 1
        elif 41 <= i <= 50:
            ranges['41-50 cm'] += 1
    
    # Setting up the bar chart
    labels = list(ranges.keys()) # xlabel, keys are the data in ranges like 0-10cm
    counts = list(ranges.values()) #ylabel, values are value lol

    # Plot it
    plt.bar(labels, counts)
    plt.xlabel('Snowfall range in cm')
    plt.ylabel('Number of time it appeared')
    plt.title('Snowfall Occurences')
    plt.show()

graphSnowfall('q2.txt')