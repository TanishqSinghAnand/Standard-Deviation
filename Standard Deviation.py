import math
import csv

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
data = file_data[0]
data2 = []
for i in file_data:
    idk = int(i[0])
    data2.append(idk)
    print(data2)


def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    mean = total/n
    print(mean)
    return mean


squared_list = []
for num in data2:
    a = int(num) - mean(data2)
    a = a**2
    squared_list.append(a)

sum = 0
for j in squared_list:
    sum = sum+j

print(len(data))
result = sum/(len(data2)-1)

std_deviaton = math.sqrt(result)
print(std_deviaton)
