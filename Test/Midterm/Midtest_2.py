class_num, rate = input().split(",")
class_num = int(class_num)
rate = int(rate)

total_str = input().split(",")
total = [0] * class_num
for i in range(class_num):
    total[i] = int(total_str[i])


effective_str = input().split(",")
effective = [0] * class_num
for i in range(class_num):
    effective[i] = int(effective_str[i])

score = []
for i in range(class_num):
    score.append(input().split(","))
    for j in range(len(score[i])):
        score[i][j] = int(score[i][j])

passed_count = 0
passed = [0] * class_num
for i in range(class_num):
    if effective[i] / total[i] * 100 >= rate:
        passed_count += 1
        passed[i] = 1

sum = 0
max = max_class = max_student = max_score = -1
if passed_count == 0:
    print(-1)
else:
    for i in range(class_num):
        if passed[i] == 1:
            for j in range(len(score[i])):
                sum += score[i][j]
        average = sum / effective[i]
        if average > max:
            max = average
            max_class = i + 1
            max_student = total[i]
            max_score = sum
        sum = 0
print(max_class, max_student, max_score, sep=",")
