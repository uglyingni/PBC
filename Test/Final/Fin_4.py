search = input()
content = input()
count = 0
 
for i in range(len(content)-len(search)+1):
    new_content = ""
    for j in range(len(search)):
        if search[j] == "?":
            new_content += "?"
        else:
            new_content += content[i+j]
    if search == new_content:
        print(content[i:i+len(search)])
        count += 1

if count == 0:
    print("^^^NOT_FOUND^^^")
