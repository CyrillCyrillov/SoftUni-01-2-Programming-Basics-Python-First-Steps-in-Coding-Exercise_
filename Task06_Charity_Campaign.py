days = int(input())
confectioners = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
income = (cakes * 45 + waffles * 5.8 + pancakes * 3.2) * confectioners * days
sum = income - income / 8
print(sum)
