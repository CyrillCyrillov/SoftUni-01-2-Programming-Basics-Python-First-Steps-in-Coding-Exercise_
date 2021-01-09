length = int(input())
width = int(input())
height = int(input())
volume_percent = float(input())
volume = length / 10 * width / 10 * height / 10
water = volume - (volume * volume_percent / 100)
print(water)
