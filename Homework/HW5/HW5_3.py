n = int(input())  # 輸入節點
edges = []
# 持續讀取關係對直到遇到STOP為止
while True:
    adj = input()
    if adj == "STOP":
        break
    else:
        edges.append([int(x) for x in adj.split(",")])


# 創立一個鄰接矩陣，並將edges中的節點關係寫進矩陣，當值為1代表兩個節點有關係，值為0代表兩個節點沒有關係
def to_adj_mat(edges, n=0):
    # 若n為0，必須依照在edges中的最大值推算n
    if n == 0:
        maxi = max(edges[i][1] for i in range(len(edges))) + 1
        to_adj_mat = [[0] * maxi for i in range(maxi)]
    else:
        # 若n為正整數但edges中包含無法用現有鄰接矩陣表示的關係，則回傳None
        for i in range(len(edges)):
            if edges[i][0] > n-1 or edges[i][1] > n-1:
                return None
        to_adj_mat = [[0] * n for i in range(n)]
    for i in range(len(edges)):
        to_adj_mat[edges[i][0]][edges[i][1]] = to_adj_mat[edges[i][1]][edges[i][0]] = 1
    return to_adj_mat


to_adj_mat = to_adj_mat(edges, n)
if to_adj_mat is None:
    print("None")
else:
    for i in range(len(to_adj_mat)):
        print(*to_adj_mat[i], sep=",")
