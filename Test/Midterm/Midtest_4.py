spot, capacity = input().split(",")
spot = int(spot)
capacity = int(capacity)

total = 0
num = [0] * spot
num_str = input().split(",")
for i in range(spot):
    num[i] = int(num_str[i])
    total += num[i]

matrix = []
for i in range(spot+1):
    matrix.append(input().split(",")
    for j in range(spot+1):
        matrix[i][j] = int(matrix[i][j])


unsaved = 0



min = 1000
while unsaved > 0:

    remain = capacity
    spot = 0

    for i in range(0, spot+1):
        for j in range(0, spot+1):
            if i != j and (i == spot or j == spot):
                distance = matrix[spot][i] - matrix[spot][]
                    min = 
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
