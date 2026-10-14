import math as m

training_data = [
    [2, 4],
    [2, 3],
    [5, 2],
    [6, 4],
    [5, 2.5],
    [2.5, 3.5]
]

n = len(training_data)

c1 = [2,4]
c2 = [5,2]

cluster_1 = []
cluster_2 = []

while True:
    cluster_1.clear()
    cluster_2.clear()

    for i in range(n):
        x = training_data[i][0]
        y = training_data[i][1]

        a1 = c1[0]
        a2 = c1[1]

        b1 = c2[0]
        b2 = c2[1]

        d1 = m.sqrt(pow(x-a1,2)+pow(y-a2,2))
        d2 = m.sqrt(pow(x-b1,2)+pow(y-b2,2))

        if d1 < d2:
            cluster_1.append(training_data[i])
        else:
            cluster_2.append(training_data[i])

    a1_avg = sum([x[0] for x in cluster_1])/len(cluster_1)
    a2_avg = sum([x[1] for x in cluster_1])/len(cluster_1)

    b1_avg = sum([x[0] for x in cluster_2])/len(cluster_2)
    b2_avg = sum([x[1] for x in cluster_2])/len(cluster_2)

    new_c1 = [a1_avg, a2_avg]
    new_c2 = [b1_avg, b2_avg]

    if c1 == new_c1 and c2 == new_c2:
        break

    c1 = new_c1
    c2 = new_c2






print(cluster_1)
print(cluster_2)
