import datetime, csv

start, end = input().split()
start = datetime.datetime.strptime(start, "%H:%M:%S")
end = datetime.datetime.strptime(end, "%H:%M:%S")


class record:
    pass


def StrToRecord(aline):
    r = record()
    r.problem = int(aline[2])
    r.status = aline[3]
    r.submission = datetime.datetime.strptime(aline[6], "%H:%M:%S")
    return r


rdict = dict()

file = "C:\\Users\\User\\Desktop\\python\\期中考批改紀錄_資料檔.csv"
fh1 = open(file, "r", encoding="utf-8", newline="")
cheader = fh1.readline()
reader1 = csv.reader(fh1)
for aline in reader1:
    R = StrToRecord(aline)
    if start <= R.submission and end >= R.submission:
        if R.problem not in rdict:
            rdict[R.problem] = [R.status]
        else:
            rdict[R.problem].append(R.status)
fh1.close()

output = ""
for key in rdict.keys():
    A = rdict[key].count("Accepted")
    C = rdict[key].count("Compile Error")
    R = rdict[key].count("Runtime Error")
    T = rdict[key].count("Time Limit Exceed")
    W = rdict[key].count("Wrong Answer")
    output += str(A) + " " + str(C) + " " + str(R) + " " + str(T) + " " + str(W) + ";"
print(output)
