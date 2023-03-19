n, m = input().split()
n = [1] * int(n)  # n面牆壁的原始顏色(1)
m = int(m)  # 油漆m次

start_end_i = []  # 每一次起始油漆的牆壁&結束油漆的牆壁&油漆的顏色
for i in range(m):
    start_end_i.append(input().split())
    for j in range(3):
        start_end_i[i][j] = int(start_end_i[i][j])

output = str()
for i in range(m):
    for j in range(start_end_i[i][0], start_end_i[i][1] + 1):
        n[j] = start_end_i[i][2]

for i in range(m):
    output += str(n.count(start_end_i[i][2])) + " " + str(start_end_i[i][2]) + ";"

print(output.strip(";"))
