type, line = input().split(",")
type = int(type)
line = int(line)

toy_list = [[int(x) for x in input().split(",")] for y in range(line)]

id_list = [0] * type
for t in range(type):
    id_list[t] = t

sum_list = [0] * type
for t in range(type):
    sum = 0
    for l in range(line):
        sum += toy_list[l][t]
    sum_list[t] = sum

idle = 0
finish = 0
idle_time = 0
finish_list = [0] * type

for x in range(0, type):
    for y in range(x+1, type):
        if sum_list[y] < sum_list[x]:
            id_list[x], id_list[y] = id_list[y], id_list[x]
            sum_list[x], sum_list[y] = sum_list[y], sum_list[x]
            for z in range(line):
                toy_list[z][x], toy_list[z][y] = toy_list[z][y], toy_list[z][x]
        elif sum_list[y] == sum_list[x]:
            if toy_list[0][y] < toy_list[0][x]:
                id_list[x], id_list[y] = id_list[y], id_list[x]
                sum_list[x], sum_list[y] = sum_list[y], sum_list[x]
                for z in range(line):
                    toy_list[z][x], toy_list[z][y] = toy_list[z][y], toy_list[z][x]
            elif toy_list[0][y] == toy_list[0][x]:
                if id_list[y] < id_list[x]:
                    id_list[x], id_list[y] = id_list[y], id_list[x]
                    sum_list[x], sum_list[y] = sum_list[y], sum_list[x]
                    for z in range(line):

                        toy_list[z][x], toy_list[z][y] = toy_list[z][y], toy_list[z][x]
for i in range(type):
    finish += toy_list[0][i]
    finish_list[i] = finish

for i in range(1, line):
    work_time = 0
    for j in range(type):
        work_time += toy_list[i][j]
        if j == 0:
            finish_list[j] += toy_list[i][j]
        elif finish_list[j-1] < finish_list[j]:
            finish_list[j] += toy_list[i][j]
        else:
            finish_list[j] = finish_list[j-1] + toy_list[i][j]
    idle_time += finish_list[type-1] - work_time


for i in range(type):
    for j in range(type):
        if id_list[j] == i:
            print(finish_list[j], end=",")
print(idle_time)
