inlist = [float(x) for x in input().split(",")]  # 輸入水位高度歷史資料
k = int(input())  # 輸入k值


# 判斷是否為谷底期，需符合前面k期水位連續下降，後面k期水位連續上升，且前後的k+1期要有額外的轉折
def find_troughs_wings(inlist, k=2):
    troughs = []
    for i in range(k+1, len(inlist)-k-1):
        if all(inlist[i-j] < inlist[i-j-1] and inlist[i+j] < inlist[i+j+1] for j in range(k)) \
          and inlist[i-k] > inlist[i-k-1] and inlist[i+k] > inlist[i+k+1]:
            troughs.append(i)
    return troughs if troughs else None


# 若k值小於1，則k為預設值2
if k >= 1:
    troughs = find_troughs_wings(inlist, k)
else:
    troughs = find_troughs_wings(inlist)

# 若find_troughs回傳None，則印出NA。若find_troughs回傳谷底期，則將期數印出
if troughs is None:
    print("NA")
else:
    print(*troughs, sep="\n")
