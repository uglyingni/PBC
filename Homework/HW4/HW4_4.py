# 輸入玩具數量與生產線數量
type, line = input().split(",")
type = int(type)
line = int(line)

# 輸入每個玩具[t]在每一生產線[n]所花費的時間
toy_list = [[int(x) for x in input().split(",")] for y in range(line)]

# 決定第一個生產的玩具
order_list = [0] * type
least0 = 10000
for i in range(type):
    idle0 = 0
    for j in range(line):
        idle0 += toy_list[j][i] * (line - j - 1)
    if idle0 < least0:
        least0 = idle0
        order_list[0] = i

# 建立finish_list，以生產線為單位，儲存已經確定生產順位玩具的完成時間
finish_list = []
finish = 0
for i in range(line):
    finish += toy_list[i][order_list[0]]
    finish_list.append(finish)

# 建立remove_list，若決定好生產順位的玩具將會被移除
remove_list = []
for i in range(type):
    remove_list.append(i)
remove_list.remove(order_list[0])

finish = [0] * line
for x in range(1, type):  # 決定生產順位
    least1 = 10000
    for y in remove_list:  # 從尚未決定順位的玩具中挑選
        idle1 = 0
        for z in range(line):  # 計算玩具在跑完全部生產線所需的閒置時間
            if z == 0:
                finish[z] = finish_list[z] + toy_list[z][y]
            elif finish_list[z] < finish[z-1]:
                idle1 += finish[z-1] - finish_list[z]
                finish[z] = finish[z-1] + toy_list[z][y]
            else:
                finish[z] = finish_list[z] + toy_list[z][y]
        if idle1 < least1:
            least1 = idle1
            order_list[x] = y

    # 儲存已經確定生產順位玩具的完成時間
    for z in range(line):
        if z == 0:
            finish_list[z] += toy_list[z][order_list[x]]
        elif finish_list[z] < finish_list[z-1]:
            finish_list[z] = finish_list[z-1] + toy_list[z][order_list[x]]
        else:
            finish_list[z] += toy_list[z][order_list[x]]
    remove_list.remove(order_list[x])

idle = 0
finish = 0
idle_time = 0
finish_time = [0] * type

# 根據order_list計算每個玩具完成生產的時間和總閒置時間
for i in range(type):
    finish += toy_list[0][order_list[i]]
    finish_time[i] = finish
for i in range(1, line):
    work_time = 0
    for j in range(type):
        work_time += toy_list[i][order_list[j]]
        if j == 0:
            finish_time[j] += toy_list[i][order_list[j]]
        elif finish_time[j-1] < finish_time[j]:
            finish_time[j] += toy_list[i][order_list[j]]
        else:
            finish_time[j] = finish_time[j-1] + toy_list[i][order_list[j]]
    idle_time += finish_time[type-1] - work_time

# 按玩具序號輸出玩具完成生產的時間和總閒置時間
for i in range(type):
    for j in range(type):
        if order_list[j] == i:
            print(finish_time[j], end=",")
print(idle_time)
