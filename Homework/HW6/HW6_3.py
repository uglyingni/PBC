def output(content):
    output = ""
    listed = "01234566789.,%"
    for i in range(len(content)):
        # 若第i個字元不是數字，直接印出
        if content[i] not in listed:
            output += content[i]
        # 若第i個字元是數字，考量前後是否也為數字
        else:
            # 若是第0位字元或第i位字元前面不是數字，先加上<<再印出
            if i == 0 or content[i-1] not in listed:
                output += "<<"
            # 若前面也是數字，直接印出
            output += content[i]
            # 若是最後字元或第i位字元後面不是數字，先印出再加上>>
            if i == len(content)-1 or content[i+1] not in listed:
                output += ">>"
    print(output)


content = input()
output = output(content)
