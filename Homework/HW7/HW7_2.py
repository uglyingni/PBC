def tochar(string):
    return chr(int("0x"+string, 16))


def search(target, fh1, fh2):
    count, count1, count2, cns, output = set(), set(), set(), set(), list()
    for line in fh1:
        line = line.strip("\n").split("\t")
        count1.add(line[0])
        count2.add(line[0]+line[1])
        if target == tochar(line[1]):
            cns.add(line[0])
    cns = list(sorted(cns))
    for line in fh2:
        line = line.strip("\n").split("\t")
        count.add(line[0])
        if line[0] in cns:
            output.append([cns.index(line[0]), line[1]])
    output.sort()

    if len(count1) != len(count2):
        print("MAPPING_TABLE_ERROR")
    elif cns and output:
        out = []
        for x in output:
            if x[1] not in out:
                out.append(x[1])
        print(len(count), *out, sep="\n")
    elif cns:
        print(len(count), "NO_PHONETIC_DATA", sep="\n")
    else:
        print(len(count), "NO_CNS_DATA", sep="\n")


# line = "C:\\Users\\User\Desktop\\python\\Homework\\HW7\\PBC111-2_hw07_assisting_data"
# fn1 = line + input().strip(".").replace("/", "\\")
# fn2 = line + input().strip(".").replace("/", "\\")
fh1 = open(input(), "r", encoding="utf-8")
fh2 = open(input(), "r", encoding="utf-8")
target = input()
search(target, fh1, fh2)
fh1.close()
fh2.close()
