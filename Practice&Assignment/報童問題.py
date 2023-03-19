'''
c = int(input("單位進貨成本:"))
r = int(input("單位零售價格:"))
N = int(input("需求可能個數:"))
q = int(input("訂貨量:"))
Prob0 = float(input("賣出零份報紙機率:"))
Prob1 = float(input("賣出一份報紙機率:"))
Prob2 = float(input("賣出二份報紙機率:"))
Prob3 = float(input("賣出三份報紙機率:"))
Prob4 = float(input("賣出四份報紙機率:"))
Prob5 = float(input("賣出五份報紙機率:"))
Prob6 = float(input("賣出六份報紙機率:"))
Prob7 = float(input("賣出七份報紙機率:"))
Prob8 = float(input("賣出八份報紙機率:"))

D = 0  # 預期需求量
Profit = 0  # 預期利潤

for Prob in Prob0, Prob1, Prob2, Prob3, Prob4, Prob5, Prob6, Prob7, Prob8:
    if q > D:
        Profit += (r * D - c * q) * Prob #在賣出幾份報紙情況下的預期利潤
        D += 1
    else:
        Profit += (r * D - c * q) * Prob #預期需求量最大就是訂購量

print(int(Profit))
'''
'''
c = int(input("單位進貨成本:"))
r = int(input("單位零售價格:"))
N = int(input("需求可能個數:"))
Prob0 = float(input("賣出零份報紙機率:"))
Prob1 = float(input("賣出一份報紙機率:"))
Prob2 = float(input("賣出二份報紙機率:"))
Prob3 = float(input("賣出三份報紙機率:"))
Prob4 = float(input("賣出四份報紙機率:"))
Prob5 = float(input("賣出五份報紙機率:"))
Prob6 = float(input("賣出六份報紙機率:"))
Prob7 = float(input("賣出七份報紙機率:"))
Prob8 = float(input("賣出八份報紙機率:"))

Maxprofit = 0.0  # 最佳利潤
Maxq = 0  # 最佳訂購量

for q in range(9):  # 在不同訂購量下計算出最佳利潤
    Profit = 0  # 預期利潤歸零，才不會一直往上加
    D= 0  # 預期需求量歸零
    for Prob in Prob0, Prob1, Prob2, Prob3, Prob4, Prob5, Prob6, Prob7, Prob8:
        if q > D:
            Profit += (r * D - c * q) * Prob
            D += 1
        else:
            Profit += (r * D - c * q) * Prob
        if Profit > Maxprofit:
            Maxprofit = Profit
            Maxq = q  # 從小計算到大，不會發生預期利潤相同但訂購量不同的情況

print(Maxq, int(Maxprofit))
'''
'''
c = int(input("單位進貨成本:"))
r = int(input("單位零售價格:"))
N = int(input("需求可能個數:"))
Problist = []
for Prob in range(N+1):
    Problist.append(float(input()))

Maxprofit = 0.0  # 最佳利潤
Maxq = 0  # 最佳訂購量

for q in range(N+1):  # 在不同訂購量下計算出最佳利潤
    Profit = 0  # 預期利潤歸零，才不會一直往上加
    D = 0  # 預期需求量歸零
    for Prob in Problist:
        if q > D:
            Profit += (r * D - c * q) * Prob
            D += 1
        else:
            Profit += (r * D - c * q) * Prob
        if Profit > Maxprofit:
            Maxprofit = Profit
            Maxq = q  # 從小計算到大，不會發生預期利潤相同但訂購量不同的情況

print(Maxq, int(Maxprofit))
'''
# 有殘值
c = int(input())
r = int(input())
N = int(input())
s = int(input())

Problist = []
# check = 0.0
for Prob in range(N+1):
    Problist.append(float(input()))

Maxprofit = 0.0  # 最佳利潤
Maxq = 0  # 最佳訂購量

for q in range(N+1):  # 在不同訂購量下計算出最佳利潤
    Profit = 0  # 預期利潤歸零，才不會一直往上加
    D = 0  # 預期需求量歸零
    for Prob in Problist:
        if q > D:
            Profit += (r * D - c * q) * Prob + (q - D) * s * Prob
            D += 1
        else:
            Profit += (r * D - c * q) * Prob
        if Profit > Maxprofit:
            Maxprofit = Profit
            Maxq = q  # 從小計算到大，不會發生預期利潤相同但訂購量不同的情況

print(Maxq, int(Maxprofit))
