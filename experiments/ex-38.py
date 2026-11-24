data = [2, 3, 4, 10, 11, 12]
k = 2

c1 = 2
c2 = 10

for i in range(5):
    cluster1 = []
    cluster2 = []

    for x in data:
        if abs(x - c1) < abs(x - c2):
            cluster1.append(x)
        else:
            cluster2.append(x)

    c1 = sum(cluster1) / len(cluster1)
    c2 = sum(cluster2) / len(cluster2)

print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
