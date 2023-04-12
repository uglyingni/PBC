n1, n2 = input().split(",")
n1 = int(n1)
n2 = int(n2)
line1 = input().split(",")
line2 = input().split(",")
list1 = [0] * n1
list2 = [0] * n2
sum1 = sum2 = 0
for i in range(n1):
    list1[i] = int(line1[i])
    sum1 += list1[i]
for i in range(n2):
    list2[i] = int(line2[i])
    sum2 += list2[i]

if sum1/n1 == sum2/n2:
    print(0)
elif sum1/n1 > sum2/n2:
    print(1)
else:
    print(2)
