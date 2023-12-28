import random


# 1~50
# 使用者 猜五次
# 猜對 提前離開
# 猜錯 提示答案

# 題目
# 提示區間(1~50)->(1~25)....

start = 1
end = 50

x = random.randint(start, end)
print(f"範圍:{start},{end}")
# print(x)


for i in range(5):
    y = eval(input(f'請猜數字({start},{end}):'))
    if i == 4:
        print('次數用完了')
    else:
        if y == x:
            print('猜對了！')
            break
        else:
            if y > x:
                print('猜低一點')
                if end > y:
                    end = y - 1
            else:
                if start < y:
                    start = y + 1
                print('猜高一點')

if y != x:
    print(f"答案為:{x}")
else:
    print(f"恭喜過關,共猜{i+1}次")
