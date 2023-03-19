import math

x1 = int(input())  # 輸入鳳黃禮盒數量
x2 = int(input())  # 輸入傳統禮盒數量
y1 = int(input())  # 輸入蛋黃酥生產力
y2 = int(input())  # 輸入鳳梨酥生產力

output1 = x1*2 + x2*3  # 蛋黃酥製作數量
output2 = x1*4 + x2*3  # 鳳梨酥製作數量
output3 = output1 / y1  # 蛋黃酥製作人力
output4 = output2 / y2  # 鳳梨酥製作人力

print(str(output1) + "," + str(output2) + "," + str(math.ceil(output3)) + "," + str(math.ceil(output4)))
