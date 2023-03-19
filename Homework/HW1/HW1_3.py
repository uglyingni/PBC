box1 = int(input())  # 輸入鳳黃禮盒數量
box2 = int(input())  # 輸入傳統禮盒數量
yolk_prod = int(input())  # 輸入蛋黃酥生產力
pine_prod = int(input())  # 輸入鳳梨酥生產力
type1_wage = int(input())  # 輸入一類員工薪資
type2_wage = int(input())  # 輸入二類員工薪資
os_yolk = int(input())  # 輸入外包蛋黃酥單價
os_pine = int(input())  # 輸入外包鳳梨酥單價

yolk = box1*2 + box2*3  # 蛋黃酥製作數量
pine = box1*4 + box2*3  # 鳳梨酥製作數量

# 聘請盡量多的一類員工後，計算剩餘蛋黃酥與鳳梨酥數量，並設定其餘變數
type1_num = yolk//yolk_prod + pine//pine_prod
rest_yolk = yolk % yolk_prod
rest_pine = pine % pine_prod
type2_num = 0
outsource = 0

# 決定剩餘蛋黃酥與鳳梨酥是指派一類員工或二類員工或外包來完成
# 如皆無剩餘，則已完成指派
if rest_yolk == 0 and rest_pine == 0:
    pass
# 如其中之一有剩餘，因為p2>p1，所以只須比較聘請一位一類員工與外包之金額
elif rest_yolk == 0 or rest_pine == 0:
    if rest_yolk == 0:
        if rest_pine * os_pine > type1_wage:
            type1_num += 1
        else:
            outsource += rest_pine * os_pine
    else:
        if rest_yolk * os_yolk > type1_wage:
            type1_num += 1
        else:
            outsource += rest_yolk * os_yolk
# 如皆有剩餘，因為2p1>p2，所以排除聘請二位一類員工情境，並且比較聘請一位二類員工或聘請一位一類員工+其一外包或皆外包之金額
else:
    if rest_yolk * os_yolk > type1_wage or rest_pine * os_pine > type1_wage:
        if rest_yolk * os_yolk > type1_wage:
            if type1_wage + rest_pine * os_pine > type2_wage:
                type2_num += 1
            else:
                type1_num += 1
                outsource += rest_pine * os_pine
        else:
            if type1_wage + rest_yolk * os_yolk > type2_wage:
                type2_num += 1
            else:
                type1_num += 1
                outsource += rest_yolk * os_yolk
    else:
        if rest_yolk * os_yolk + rest_pine * os_pine > type2_wage:
            type2_num += 1
        else:
            outsource += rest_yolk * os_yolk + rest_pine * os_pine

total_cost = type1_num*type1_wage + type2_num*type2_wage + outsource  # 薪資總額

print(str(yolk) + "," + str(pine) + "," + str(total_cost))
