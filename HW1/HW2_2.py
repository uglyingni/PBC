import math

type = int(input())

pine_num = 0
yolk_num = 0
for i in range(type):
    num = int(input())
    pine_num += (i + 3) * num
    yolk_num += (i + 1) * num

pine_prod = int(input())
yolk_prod = int(input())

print(pine_num, yolk_num, (math.ceil(pine_num / pine_prod)), (math.ceil(yolk_num / yolk_prod)), sep=",")
