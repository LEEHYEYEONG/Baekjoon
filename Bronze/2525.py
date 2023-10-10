h, m = map(int, input().split())
time = int(input())

add_hour = (m + time) // 60
add_minute = (m + time) % 60

if(add_hour >= 1):
	if((h + add_hour) >= 24):
		h -= 24
	print(h+add_hour, add_minute)
else:
	print(h, m+time)