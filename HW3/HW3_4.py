# 輸入禮盒種類數、未來訂單天數、鳳梨酥生產力、蛋黃酥生產力
type, day, pine_prod, yolk_prod = input().split(",")
type = int(type)
day = int(day)
pine_prod = int(pine_prod)
yolk_prod = int(yolk_prod)

# 輸入每一種類禮盒分別含有的鳳梨酥數量
pine_list = []
pine_list.append(input().split(","))

# 輸入每一種類禮盒分別含有的蛋黃酥數量
yolk_list = []
yolk_list.append(input().split(","))

# 輸入每一種類禮盒每一天的需求量
demand_list = []
for t in range(type):
    demand_list.append(input().split(","))

for d in range(day):

    # 計算每一天鳳梨酥、蛋黃酥需求量總數（所以要先歸零）
    pine_total = 0
    yolk_total = 0

    for t in range(type):

        # 根據每一種類禮分別的需求量，去計算鳳梨酥、蛋黃酥需求量
        demand = int(demand_list[t][d])
        pine_num = int(pine_list[0][t])
        yolk_num = int(yolk_list[0][t])
        pine_total += pine_num * demand
        yolk_total += yolk_num * demand

    # 計算每一天要聘僱的人力
    employee = pine_total//pine_prod + yolk_total//yolk_prod
    if pine_total % pine_prod != 0 and yolk_total % yolk_prod != 0:
        employee += 2
    elif pine_total % pine_prod != 0 or yolk_total % yolk_prod != 0:
        employee += 1

    # 如果為最後一天就不印符號","
    if d == day - 1:
        print(employee)
    else:
        print(employee, end=",")
