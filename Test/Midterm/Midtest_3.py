station = int(input())
capacity = int(input())
passenger_str = input().split(",")
passenger_list = [0] * station
unserved = 0
for i in range(station):
    passenger_list[i] = int(passenger_str[i])
    unserved += passenger_list[i]

output = ""
while unserved > 0:

    remain = capacity

    for n in range(station):
        if passenger_list[n] != 0 and remain >= passenger_list[n]:
            remain -= passenger_list[n]
            unserved -= passenger_list[n]
            output += str(n + 1) + "," + str(passenger_list[n]) + ";"
            passenger_list[n] = 0
        elif passenger_list[n] != 0 and remain < passenger_list[n] and remain > 0:
            unserved -= remain
            passenger_list[n] -= remain
            output += str(n + 1) + "," + str(remain) + ";"
            remain = 0
    print(output.strip(";"))
    output = ""
