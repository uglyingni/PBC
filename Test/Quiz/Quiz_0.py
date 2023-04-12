line1 = input()
line1 = line1.split(",")
station = int(line1[0])
capacity = int(line1[1])

line2 = input()
line2 = line2.split(",")
passenger = [0] * station
unserved = 0
for n in range(station):
    passenger[n] = int(line2[n])
    unserved += passenger[n]

while unserved > 0:

    remain = capacity

    for n in range(station):
        if remain >= passenger[n]:
            remain -= passenger[n]
            unserved -= passenger[n]
            if n < (station - 1):
                print(passenger[n], end=",")
            else:
                print(passenger[n])
            passenger[n] = 0
        else:
            unserved -= remain
            passenger[n] -= remain
            if n < (station - 1):
                print(remain, end=",")
            else:
                print(remain)
            remain = 0
