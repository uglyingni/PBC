# ord轉chr
'''
ord_input = input().split()

ord_chr = []
for i in ord_input:
    ord_chr.append(chr(int(i)))

print(ord_chr)
'''
# chr轉ord
chr_input = input()

chr_ord = []
for i in chr_input:
    chr_ord.append(ord(i))

print(chr_ord)
# zip
'''
twid = input()

cmap = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
twid_change = str(cmap[ord(twid[0]) - 65]) + str(twid[1:])
checksum = 0
# for i in range(11):
    # checksum += int(twid_change[i]) * weight[i]

for pair in zip(twid_change, weight):
    checksum += int(pair[0]) * pair[1]

if len(twid) != 10:
    print("字元數輸入錯誤")

elif ord(twid[0]) < 65 or ord(twid[0]) > 90:
    print("第一碼輸入錯誤")

elif ord(twid[1]) < 49 or ord(twid[1]) > 50:
    print("第二碼輸入錯誤")

elif checksum % 10 != 0:
    print("輸入錯誤")

else:
    print("輸入正確")
'''
# lambda、map、zip
'''
twid = input()

cmap = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
twid_change = str(cmap[ord(twid[0]) - 65]) + str(twid[1:])

check = map(lambda pair: int(pair[0]) * pair[1], zip(twid_change, weight))
checksum = sum(check)

if len(twid) != 10:
    print("字元數輸入錯誤")

elif ord(twid[0]) < 65 or ord(twid[0]) > 90:
    print("第一碼輸入錯誤")

elif ord(twid[1]) < 49 or ord(twid[1]) > 50:
    print("第二碼輸入錯誤")

elif checksum % 10 != 0:
    print("輸入錯誤")

else:
    print("輸入正確")
'''
