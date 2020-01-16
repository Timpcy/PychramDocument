for i in range(6):
    print(i)
print("此处换一个函数")
for i in range(1,6):
    print(i)
######################
m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    print(num)
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fm // fn // fmn)


