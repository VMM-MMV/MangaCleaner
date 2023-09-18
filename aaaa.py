a = []

for i in range(20):
    a.append([x for x in range(20)])

for i in a:
    print(i)

# first
size = 10
for i in range(len(a)):
    check = 0
    for j in range(size):
        try:
            check += 1
            print(a[j][i], a[j][i+size-1], check, i, j)
        except:
            pass
        # print(check)
    if check == 10:
        print('yes')