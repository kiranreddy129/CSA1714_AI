
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(x)

mean_x = sum(x) / n
mean_y = sum(y) / n

num = 0
den = 0

for i in range(n):
    num += (x[i] - mean_x) * (y[i] - mean_y)
    den += (x[i] - mean_x) ** 2

m = num / den
c = mean_y - m * mean_x

print("Slope:", m)
print("Intercept:", c)

value = float(input("Enter X value: "))
prediction = m * value + c

print("Predicted Y value:", prediction)
