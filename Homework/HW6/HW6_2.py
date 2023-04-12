content = input()
seperate = content.translate(str.maketrans("。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !\"#$%&'()*+,-./:;<=>?@[\\]^_`{¦}~", ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"))
seperate = seperate.split(",")


def big_snake_ball(content):
    # 若一個句子中有出現"大"/"蛇"/"丸"，則句中每個字都要以"!"分開
    if "大" in content or "蛇" in content or "丸" in content:
        print(*content, sep="!", end="")
    # 若沒有，直接印出
    else:
        print(*content, sep="", end="")


length = 0
for i in range(len(seperate)):
    if i < len(seperate)-1:
        big_snake_ball(seperate[i])
        # 印出原content的分隔符號
        print(content[length+len(seperate[i])], end="")
        # length紀錄迴圈印到哪裡
        length += len(seperate[i])+1
    # 若最後一句是空字串，代表原content的最後一字是分隔符號，在倒數第二迴圈已經結束印出
    # 若最後一句不是空字串，代表原content的最後一字不是分隔符號，所以最後迴圈仍要看句子有沒有出現"大"/"蛇"/"丸"
    else:
        if seperate[i] != "":
            big_snake_ball(seperate[i])
