customer, massager = input().split(",")  # 輸入客人數量、按摩師數量
customer = int(customer)
massager = int(massager)

str_1 = input().split(",")  # 輸入服務時間
str_2 = input().split(",")  # 輸入預約時間
str_3 = input().split(",")  # 輸入服務價格

sort_list = []
for i in range(customer):
    sort_list.append([int(str_1[i]), int(str_2[i]), i, int(str_3[i])])
sort_list.sort()  # 按服務時間>預約時間>客人序號排序

massager_list = []
for i in range(massager):
    massager_list.append([0] * 360)

count = 0
counted = 0
income = 0
for i in range(customer):
    least = 30
    who = -1
    for j in range(massager):
        error = 0
        wait = massager_list[j][sort_list[i][1]]
        # 如果超過工作時間，error = 1
        if sort_list[i][1] + sort_list[i][0] + wait > 360 or \
            sort_list[i][1] + sort_list[i][0] > 360 or \
                sort_list[i][1] + wait > 360:
            error = 1
        # 如果超過等待時間，error = 2
        elif sort_list[i][1] + sort_list[i][0] + least <= 360:
            for u in range(least+1):
                if wait > least:
                    error = 2
                    break
                elif counted == sort_list[i][0] - 1:
                    break
                for n in range(sort_list[i][0]):
                    if massager_list[j][sort_list[i][1]+wait+n] != 0:
                        wait += massager_list[j][sort_list[i][1]+wait+n] + n
                        break
                    else:
                        counted += 1
        # 如果有空時間少於服務時間，error = 3
        else:
            for n in range(sort_list[i][0]):
                if n < sort_list[i][0] and \
                  massager_list[j][sort_list[i][1]+wait+n] != 0:
                    error = 3
                    break
        if error == 0 and wait < least + 1:
            least = wait
            who = j
    # 印上服務此客人的剩餘服務時間（對之後客人來說是等待時間）
    if who >= 0:
        for n in range(sort_list[i][0]):
            massager_list[who][sort_list[i][1]+least+n] = sort_list[i][0] - n
        count += 1
        income += sort_list[i][3]

print(count, income, sep=",")
