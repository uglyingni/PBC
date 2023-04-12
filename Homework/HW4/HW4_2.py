type = int(input())
assemble_list = [int(x) for x in input().split(",")]
package_list = [int(x) for x in input().split(",")]

finish_list = [0] * type
idle = finish = assemble = package = 0

time_with_id = [[assemble_list[i]+package_list[i], assemble_list[i], package_list[i], i] for i in range(type)]
time_with_id.sort()

for n in range(type):
    if n == 0:
        idle += time_with_id[n][1]
        finish += idle + time_with_id[n][2]
    else:
        assemble += time_with_id[n][1]
        package += time_with_id[n-1][2]
        finish += time_with_id[n][2]
        if assemble > package:
            idle += assemble - package
            finish += assemble - package
            assemble = package = 0
    finish_list[n] = finish

for i in range(type):
    for j in range(type):
        if time_with_id[j][3] == i:
            print(finish_list[j], end=",")
print(idle)
