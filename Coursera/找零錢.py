'''
change = 1000 - int(input())

result = str()

if change//500 > 0:
    result = "500, " + str(change//500)

    if change%500//100 > 0:
        result += "; 100, " + str(change%500//100)

    if change%100//50 > 0:
        result += "; 50, " + str(change%100//50)

    if change%50//10 > 0:
        result += "; 10, " + str(change%50//10)

    if change%10//5 > 0:
        result += "; 5, " + str(change%10//5)

    if change%5 > 0:
        result += "; 1, " + str(change%5)

elif change%500//100 > 0:
    result = "100, " + str(change%500//100)

    if change%100//50 > 0:
        result += "; 50, " + str(change%100//50)

    if change%50//10 > 0:
        result += "; 10, " + str(change%50//10)

    if change%10//5 > 0:
        result += "; 5, " + str(change%10//5)

    if change%5 > 0:
        result += "; 1, " + str(change%5)

elif change%100//50 > 0:
    result = "50, " + str(change%100//50)

    if change%50//10 > 0:
        result += "; 10, " + str(change%50//10)

    if change%10//5 > 0:
        result += "; 5, " + str(change%10//5)

    if change%5 > 0:
        result += "; 1, " + str(change%5)

elif change%50//10 > 0:
    result = "10, " + str(change%50//10)

    if change%10//5 > 0:
        result += "; 5, " + str(change%10//5)

    if change%5 > 0:
        result += "; 1, " + str(change%5)

elif change%10//5 > 0:
    result = "5, " + str(change%10//5)

    if change%5 > 0:
        result += "; 1, " + str(change%5)

elif change%5 > 0:
    result = "1, " + str(change%5)

print(result)
'''
# if-else:
'''
change = 1000 - int(input())

num1 = change//500
num2 = change%500//100
num3 = change%100//50
num4 = change%50//10
num5 = change%10//5
num6 = change%5

result = str()

if num1 > 0:
    result += "500, " + str(num1)

if num2 > 0:
    if num1 == 0:
        result += "100, " + str(num2)
    else:
        result += "; 100, " + str(num2)

if num3 > 0:
    if num1 == 0 and num2 == 0:
        result += "50, " + str(num3)
    else:
        result += "; 50, " + str(num3)

if num4 > 0:
    if num1 == 0 and num2 == 0 and num3 == 0:
        result += "10, " + str(num4)
    else:
        result += "; 10, " + str(num4)

if num5 > 0:
    if num1 == 0 and num2 == 0 and num3 == 0 and num4 == 0:
        result += "5, " + str(num5)
    else:
        result += "; 5, " + str(num5)

if num6 > 0:
    if num1 == 0 and num2 == 0 and num3 == 0 and num4 == 0 and num5 == 0:
        result += "1, " + str(num6)
    else:
        result += "; 1, " + str(num6)

print(result)
'''
'''
change = 1000 - int(input())

num1 = change//500
num2 = change%500//100
num3 = change%100//50
num4 = change%50//10
num5 = change%10//5
num6 = change%5

result = str()

if num1 > 0:
    result += "500, " + str(num1)

if num2 > 0:
    result += "; 100, " + str(num2)

if num3 > 0:
    result += "; 50, " + str(num3)

if num4 > 0:
    result += "; 10, " + str(num4)

if num5 > 0:
    result += "; 5, " + str(num5)

if num6 > 0:
    result += "; 1, " + str(num6)

print(result.strip(";"))
'''
# iteration:
change = 1000 - int(input())

result = str()

for money in 500, 100, 50, 10, 5, 1:
    if change//money > 0:
        result += str(money) + ", " + str(change//money) + "; "
        change -= change//money*money

print(result[:-2])
