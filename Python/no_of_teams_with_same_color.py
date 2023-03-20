n = int(input(""))
home_codes = [0] * 101
guest_codes = [0] * 101

for i in range(n):
    home, guest = input("").split(" ")
    home = int(home)
    guest = int(guest)
    home_codes[home] += 1
    guest_codes[guest] += 1

count = 0

for i in range(1, 101):
    count += home_codes[i] * guest_codes[i]

print(count)
