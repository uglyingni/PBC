s1 = input()  # 輸入字串一
s2 = input()  # 輸入字串二
d = int(input())  # 輸入距離限制
content = input()  # 輸入文件內容

# d為整數且需介於0~1000之間，s1、s2、content長度需介於1~10000之間
if d < 0 or d > 1000 or \
      len(s1) == 0 or len(s2) == 0 or len(content) == 0 or \
        len(s1) > 10000 or len(s2) > 10000 or len(content) > 10000:
    print("ILLEGAL_INPUT")
# 搜尋並印出文件中出現s1與s2且間隔小於d的句子
else:
    count = 0
    for x in range(len(content)):
        if all(s1[y] == content[x+y] for y in range(len(s1))):
            for z in range(d):
                if x+z+len(s1+s2) <= len(content) and \
                  all(s2[y] == content[x+y+z+len(s1)] for y in range(len(s2))):
                    count += 1
                    print(content[x:x+z+len(s1+s2)])
        elif all(s2[y] == content[x+y] for y in range(len(s2))):
            for z in range(d):
                if x+z+len(s1+s2) <= len(content) and \
                  all(s1[y] == content[x+y+z+len(s2)] for y in range(len(s1))):
                    count += 1
                    print(content[x:x+z+len(s1+s2)])
    if count == 0:
        print("^^NOT_FOUND^^")
