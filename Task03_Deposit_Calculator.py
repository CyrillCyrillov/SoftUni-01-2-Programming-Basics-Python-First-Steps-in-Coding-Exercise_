deposit = float(input())
mounts = int(input())
interest_rate = float(input())
suma = deposit + mounts * ((deposit * interest_rate / 100) / 12)
print(suma)
