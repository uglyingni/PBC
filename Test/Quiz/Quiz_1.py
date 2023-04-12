line1 = int(input())
line2 = int(input())

if line2 % line1 == 0:
    print(1)
elif line1 % line2 == 0:
    print(2)
else:
    print(3)
