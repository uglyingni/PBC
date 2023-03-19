day = int(input())

total_stock = 0
out_of_stock = 0
for i in range(day):
    stock = int(input())
    total_stock += stock
    if total_stock < 0 and out_of_stock == 0:
        out_of_stock = i + 1

# 如果第a天曾缺貨，印a
if out_of_stock != 0:
    print(out_of_stock)
# 如果從未缺貨，印最後一天的存貨數
else:
    print(total_stock)
