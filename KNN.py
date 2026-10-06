import math as m

training_data = [
    [4.2, 2.8, 1], 
    [4.0, 2.0, 1], 
    [3.8, 0.5, 1], 
    [2.0, 1.5, 1], 
    [2.7, 2.5, 1], 
    [1.7, 3.2, 0], 
    [2.7, 4.0, 0], 
    [1.2, 5.2, 0], 
    [2.2, 6.2, 0], 
    [0.3, 6.2, 0]
]

x1 = 2.2
x2 = 3

for i in range(10):
    x = m.sqrt(m.pow((x1-training_data[i][0]), 2) + m.pow((x2-training_data[i][1]), 2))
    training_data[i].append(x)

sorted_data = sorted(training_data, key=lambda x: x[3])

while True:
    dog = 0
    cat = 0
    r = int(input("Enter k = "))
    if(r > 10):
        print("The k is large than the data set. Provide less than or equal 10.")
        continue

    for i in range(r):
        if sorted_data[i][2]:
            dog+=1
        else:
            cat+=1
    print("Dog" if dog>=cat else "Cat")


