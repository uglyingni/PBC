import math

x1 = int(input())  # 輸入鳳黃禮盒數量
x2 = int(input())  # 輸入傳統禮盒數量
y1 = int(input())  # 輸入蛋黃酥生產力
y2 = int(input())  # 輸入鳳梨酥生產力
p1 = int(input())  # 輸入一類員工薪資
p2 = int(input())  # 輸入二類員工薪資

output1 = x1*2 + x2*3  # 蛋黃酥製作數量
output2 = x1*4 + x2*3  # 鳳梨酥製作數量
output3 = math.ceil(output1 / y1)  # 一類員工聘請人數(蛋黃酥)
output4 = math.ceil(output2 / y2)  # 一類員工聘請人數(鳳梨酥)
output5 = math.ceil((output1 % y1 * y1 + output2 % y2 * y2) / (y1 * y2))  # 二類員工聘請人數

# 選擇出二類員工聘請人數最少的方案
if output5 // 2 > 0 or output1 % y1 == 0 or output2 % y2 == 0:
    output5 = 0
else:
    output3 = output1 // y1
    output4 = output2 // y2

output6 = (output3 + output4)*p1 + output5*p2  # 薪資總額

print(str(output1) + "," + str(output2) + "," + str(output3) + "," + str(output4) + "," + str(output5) + "," + str(output6))
