import math

day = int(input())  # 輸入規劃人力聘僱與配置的天數
add_num = int(input())  # 輸入禮盒需求量的每日增加數
pineyolk_box = int(input())  # 輸入第一日鳳黃禮盒的需求量
trandition_box = int(input())  # 輸入第一日傳統禮盒的需求量
pine_prod = int(input())  # 輸入鳳梨酥生產力
yolk_prod = int(input())  # 輸入蛋黃酥生產力

# 逐日根據調整後的禮盒需求量、分別算出鳳梨酥與蛋黃酥所需聘僱的人力
for i in range(day):
    pine = 4*pineyolk_box + 3*trandition_box
    yolk = 2*pineyolk_box + 3*trandition_box

    print(math.ceil(pine / pine_prod), math.ceil(yolk / yolk_prod), sep=",")

    pineyolk_box = pineyolk_box + add_num
    trandition_box = trandition_box + add_num
