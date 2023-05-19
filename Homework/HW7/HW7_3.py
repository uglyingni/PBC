time_str = input()

num = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]


def adjusted(time_str, year_month_day=False):
    if time_str == 2 and year_month_day == False:
        output = "兩"
    elif time_str <= 10:
        output = num[time_str]
    elif time_str > 10 and time_str < 20:
        output = num[10] + num[time_str % 10]
    elif time_str % 10 == 0:
        output = num[time_str // 10] + num[10]
    else:
        output = num[time_str // 10] + num[10] + num[time_str % 10]
    return output


def year_month_day(time):
    output = "西元"
    time = time.split("-")
    output += num[int(time[0][0])] + num[int(time[0][1])] + num[int(time[0][2])] + num[int(time[0][3])] + "年" + adjusted(int(time[1]), True) + "月" + adjusted(int(time[2]), True) + "日"
    return output


def hour(time):
    output = ""
    time = int(time.strip("T"))
    if time < 12:
        output += "上午" + adjusted(time) + "點"
    elif time == 12:
        output += "下午" + adjusted(time) + "點"
    else:
        output += "下午" + adjusted(time-12) + "點"
    return output


def minute_or_second(time, minute_or_second):
    output = ""
    time = int(time.strip(":"))
    if time == "00":
        output += num[0] + minute_or_second
    else:
        output += adjusted(time) + minute_or_second
    return output


output = ""
if "-" in time_str:
    output += year_month_day(time_str[0:10])
if "T" in time_str:
    output += hour(time_str[time_str.index("T"):time_str.index("T")+3])
if ":" in time_str:
    output += minute_or_second(time_str[time_str.index("T")+3:time_str.index("T")+6], "分")
if time_str.count(":") == 2:
    output += minute_or_second(time_str[time_str.index("T")+6:time_str.index("T")+9], "秒")
print(output)
