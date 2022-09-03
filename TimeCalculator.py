def add_time(start, duration, day="a"):
    temp = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
    weekday = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    st = start.split()
    i_time = st[0]
    s = st[1]
    hm = i_time.split(':')
    i_h = int(hm[0])
    i_m = int(hm[1])

    div = duration.split(':')
    f_h = int(div[0])
    f_m = int(div[1])

    min_sum = f_m + i_m
    if min_sum >= 60:
        min_sum -= 60
        f_h += 1

    full_day = f_h // 24
    f_h = f_h % 24

    hrs_sum = i_h + f_h

    if 12 < hrs_sum < 24:
        hrs_sum -= 12
        if s == "PM":
            s = "AM"
            full_day += 1
        else:
            s = "PM"
    elif hrs_sum == 24 or hrs_sum == 12:
        hrs_sum = 12
        if s == "PM":
            s = "AM"
            full_day += 1
        else:
            s = "PM"
    elif hrs_sum > 24:
        hrs_sum -= 24

    if min_sum < 10:
        new_time = str(hrs_sum) + ":" + "0" + str(min_sum) + " " + s
    else:
        new_time = str(hrs_sum) + ":" + str(min_sum) + " " + s

    if day == "a":
        pass
    else:
        if full_day == 0:
            new_time += ", " + day
        else:
            index = temp.get(day)
            ans = index + (full_day % 7)
            if ans > 7:
                ans = ans % 7
            new_time += ", " + weekday[ans]

    if full_day == 1:
        new_time += " (next day)"
    elif full_day > 1:
        new_time += " (" + str(full_day) + " days later)"

    return new_time


print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "Saturday"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "Tuesday"))