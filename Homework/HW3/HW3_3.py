import math

day, pine_prod, yolk_prod = input().split(",")
day = int(day)
pine_prod = int(pine_prod)
yolk_prod = int(yolk_prod)

pineyolk_list = []
pineyolk_list.append(input().split(","))
trandition_list = []
trandition_list.append(input().split(","))

output_list = []
for i in range(day):
    pineyolk = int(pineyolk_list[0][i])
    trandition = int(trandition_list[0][i])
    pine_num = 4*pineyolk + 3*trandition
    yolk_num = 2*pineyolk + 3*trandition
    output_list.append(math.ceil(pine_num / pine_prod) + math.ceil(yolk_num / yolk_prod))

print(*output_list, sep=",")
