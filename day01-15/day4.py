import random
answer=random.randint(1,101)
counter=0
while True:
    counter+=1
    number=int(input("输入一个数字"))
    if number<answer:
        print("需要一个大一点的数字")
    elif number > answer:
        print("需要一个小一点的数字")
    elif number==answer:
        print("恭喜答对了！")
        #这里需要break 终止函数的进行 不然就算你答对了
        #依旧在循环中
        break
print("一共回答了%d次"%counter)