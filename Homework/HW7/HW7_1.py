def tochar(string):
    return chr(int("0x"+string, 16))


def search(target, fh):
    count1, count2, output = set(), set(), list()
    for line in fh:
        line = line.strip("\n").split("\t")
        count1.add(line[0])
        count2.add(line[0]+line[1])
        if target[0] == "CNS" and line[0] == target[1] and tochar(line[1]) not in output:
            output.append(tochar(line[1]))
        elif target[0] == "CHAR" and tochar(line[1]) == target[1] and line[0] not in output:
            output.append(line[0])
            output.sort()
    if len(count1) != len(count2):
        print("MAPPING_TABLE_ERROR")
    elif output:
        print(len(count2), *output, sep="\n")
    else:
        print(len(count2), "NO_DATA_FOUND", sep="\n")


# line = "C:\\Users\\User\Desktop\\python\\Homework\\HW7\\PBC111-2_hw07_assisting_data"
# fn = line + input().strip(".").replace("/", "\\")
fh = open(input(), "r", encoding="utf-8")
target = input().split(":")
search(target, fh)
fh.close()
