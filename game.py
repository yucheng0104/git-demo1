import random


# 1~50
# 使用者 猜五次
# 猜對 提前離開
# 猜錯 提示答案

# 題目
x = random.randint(1, 50)
print(x)


for i in range(5):
    y = eval(input('請猜數字(1,50): '))
    if y == x:
        print('猜對了！')
        break
    elif y < x:
        print("猜錯了 比 %2d 大" % y)
    elif y > x:
        print("猜錯了 比 %2d 小" % y)
