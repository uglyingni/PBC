def output(content):
    listed, num, output = [], [], []
    lastname = "陳林黃張李王吳劉蔡楊許鄭謝郭洪曾邱廖賴周徐蘇葉莊呂江何蕭羅高簡朱鍾施游詹沈彭胡余盧潘顏梁趙柯翁魏方孫戴范宋鄧杜侯曹薛傅丁溫紀蔣歐藍連唐馬董石卓程姚康馮古姜湯汪白田涂鄒巫尤鐘龔嚴韓黎阮袁童陸金錢邵"
    for i in range(len(content)):
        if content[i] in lastname and (content[i-1] == "姓" or content[i+1] == "姓"):
            listed.append(content[i])
        elif content[i] in lastname and ((content[i+1] == "先" and content[i+2] == "生") or (content[i+1] == "小" and content[i+2] == "姐")):
            listed.append(content[i])
    for i in range(len(listed)):
        if listed[i] not in num:
            num.append(listed[i])
            output.append([listed.count(listed[i]), 97-lastname.index(listed[i]), listed[i]])
    output = sorted(output, reverse=True)
    for i in range(len(output)):
        print(output[i][2], output[i][0], sep= ":")

content = input()
output(content)
