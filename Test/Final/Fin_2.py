# 判斷是否為谷底期，需符合前面k1期水位連續下降，後面k2期水位連續上升
def find_troughs(inlist, k1, k2):
    troughs = []
    for i in range(k1, len(inlist)-k2):
        if all(inlist[i-j] < inlist[i-j-1] for j in range(k1)) and all(inlist[i+j] < inlist[i+j+1] for j in range(k2)):
            troughs.append(i)
    return troughs if troughs else None

inlist = [float(x) for x in input().split(",")]  # 輸入水位高度歷史資料
k1 = int(input())
if k1 < 1:
    k1 = 2
k2 = int(input())
if k2 < 1:
    k2 = 2

troughs = find_troughs(inlist, k1, k2)

# 若find_troughs回傳None，則印出NA。若find_troughs回傳谷底期，則將期數印出
if troughs is None:
    print("NA")
else:
    print(*troughs, sep="\n")
