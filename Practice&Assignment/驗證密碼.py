password = input()
password_ord = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(len(password)):
    password_ord.append((ord(password[i])))

for i in range(len(password_ord)):
    if not ((password_ord[i] >= 65 and password_ord[i] <= 90) or \  # A~Z
        (password_ord[i] >= 97 and password_ord[i] <= 122) or \  # a~z
        (password_ord[i] >= 48 and password_ord[i] <= 57) or \  # 0~9
        ((password_ord[i] == 33) or (password_ord[i] >= 35 and password_ord[i] <= 38) or (password_ord[i] >= 40 and password_ord[i] <= 43) or (password_ord[i] >= 94 and password_ord[i] <= 95))):  # !@#$%^&*()_+"
        print("只能包含英文字母、數字、以及!@#$%^&*()_+")
    if (password_ord[i] >= 65 and password_ord[i] <= 90):
        count1 += 1
    if (password_ord[i] >= 97 and password_ord[i] <= 122):
        count2 += 1
    if (password_ord[i] >= 48 and password_ord[i] <= 57):
        count3 += 1
    if ((password_ord[i] == 33) or (password_ord[i] >= 35 and password_ord[i] <= 38) or (password_ord[i] >= 40 and password_ord[i] <= 43) or (password_ord[i] >= 94 and password_ord[i] <= 95)):
        count4 += 1

if (len(password) >= 8 or len(password) <= 20) and count1 >= 1 and count2 >= 1 and count3 >= 1 and count4 >= 1:
    output = "密碼有效"
else:
    output = "密碼無效"
    if len(password) < 8 or len(password) > 20:
        output += "，長度需介於8~12個字"
    if count1 < 1:
        output += "，必須包含至少一個大寫英文字母"
    if count2 < 1:
        output += "，必須包含至少一個小寫英文字母"
    if count3 < 1:
        output += "，必須包含至少一個數字"
    if count4 < 1:
        output += "，必須包含至少一個符號"

print(output)
