n = int(input())  # 輸入節點
k = int(input())  # 輸入主角節點
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


# 找出與主角節點最接近的節點編號與他們的共同節點數量
def find_closet(to_adj_mat, k):
    # 若to_adj_mat輸出None或是主角節點超出節點範圍，則回傳None
    if to_adj_mat is None or k > len(to_adj_mat) - 1:
        closest_num, closest_count = None, None
    else:
        closest_num, closest_count = 0, 0
        for i in range(len(to_adj_mat)):
            count = 0
            for j in range(len(to_adj_mat)):
                if to_adj_mat[k][j] == 1 and to_adj_mat[i][j] == 1 and k != i:
                    count += 1
            if count > closest_count:
                closest_num, closest_count = i, count
    return closest_num, closest_count


to_adj_mat = to_adj_mat(edges, n)
closest_num, closest_count = find_closet(to_adj_mat, k)
if closest_num is None and closest_count is None:
    print("None")
else:
    print(closest_num, closest_count, sep="\n")
