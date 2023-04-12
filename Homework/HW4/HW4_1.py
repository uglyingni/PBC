type = int(input())
assemble_list = [int(x) for x in input().split(",")]
package_list = [int(x) for x in input().split(",")]

finish_list = [0] * type
idle = finish = assemble = package = 0

for n in range(type):
    if n == 0:
        idle += assemble_list[n]
        finish += idle + package_list[n]
    else:
        assemble += assemble_list[n]
        package += package_list[n-1]
        finish += package_list[n]
        if assemble > package:
            idle += assemble - package
            finish += assemble - package
            assemble = package = 0
    finish_list[n] = finish

print(*finish_list, idle, sep=",")
