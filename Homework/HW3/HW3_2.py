day, group, money = input().split(",")
day = int(day)
group = int(group)
money = int(money)

bound_list = []
for i in range(2):
    bound_list.append(input().split(","))
    for j in range(group):
        bound_list[i][j] = int(bound_list[i][j])

price_list = []
price_list.append(input().split(","))
for i in range(day):
    price_list[0][i] = int(price_list[0][i])

max_money = 0
for i in range(group):
    stock = 0
    current_money = money
    for j in range(day):
        if j == (day - 1):
            current_money += stock * price_list[0][j]
        elif price_list[0][j] <= bound_list[0][i]:
            stock += int(0.5 * current_money // price_list[0][j])
            current_money -= int(0.5 * current_money // price_list[0][j] * price_list[0][j])
        elif price_list[0][j] >= bound_list[1][i]:
            current_money += int(stock // 2 * price_list[0][j])
            stock -= int(stock // 2)

    if current_money > max_money:
        max_money = current_money

print(max_money)
