line1 = int(input())
line2 = input()
line2 = line2.split(",")

count = 0
for n in range(1, line1 + 1):
    ans = int(line2[n]) % int(line2[0])
    if ans == 0:
        count += 1

if count == 0:
    print(1)
elif count == 1:
    print(2)
elif count == line1:
    print(3)
else:
    print(4)
