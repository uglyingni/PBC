day, money = input().split(",")
day = int(day)
money = int(money)

price_list = []
price_list.append(input().split(","))
for i in range(day):
    price_list[0][i] = int(price_list[0][i])

lower_bound, upper_bound = input().split(",")
lower_bound = int(lower_bound)
upper_bound = int(upper_bound)

stock = 0
for i in price_list[0]:
    if i <= lower_bound:
        stock += int(0.5 * money // i)
        money -= int(0.5 * money // i * i)
    if i >= upper_bound:
        money += int(stock // 2 * i)
        stock -= int(stock // 2)

money += stock * price_list[0][day - 1]

print(money)
