hour_one = int(input())
minute_one = int(input())
sec_one = int(input())
hour_two = int(input())
minute_two = int(input())
sec_two = int(input())
total_sec_one = sec_one + (minute_one * 60) + (hour_one * 60 * 60)
total_sec_two = sec_two + (minute_two * 60) + (hour_two * 60 * 60)
print(total_sec_two - total_sec_one)
