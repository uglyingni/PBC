n, p, d = input().split()
n = int(n)
p = int(p)
d = int(d)

town_list = []
for i in range(n):
    town_list.append(input().split())
    for j in range(3):
        town_list[i][j] = int(town_list[i][j])

set_town = ""
all_covered = 0

for p in range(p):  # 設?基地台跑?次
    current_max_covered = 0  # 第一輪跑出最佳，所以要重新歸零第二輪才能跑出次佳

    for a in range(n):
        covered = 0
        for b in range(n):
            dst = ((town_list[a][0]-town_list[b][0]) ** 2 + (town_list[a][1]-town_list[b][1]) ** 2) ** 0.5
            if dst <= d:
                covered += town_list[b][2]  # 在基地範圍內的人數加總
            if covered > current_max_covered:
                current_max_covered = covered  # 迴圈內洗出最大值
                current_max_town = a

    set_town += str(current_max_town + 1) + " "
    all_covered += current_max_covered

    for c in range(n):
        dst = ((town_list[current_max_town][0]-town_list[c][0]) ** 2 + (town_list[current_max_town][1]-town_list[c][1]) ** 2) ** 0.5
        if dst <= d:
            town_list[c][2] = 0  # 找出基地位址後，排除已經在基地範圍內的人數

print(set_town + str(all_covered))
