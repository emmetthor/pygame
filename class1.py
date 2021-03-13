import random

num=0
for i in range(1,100):
    num=random.randint(1,20)
    print("終極密碼是:"+str(num))
c=0
#print(num)
while True:    
    guess=int(input("請輸入終極密碼:"))


    if guess==num:
        print("猜對了!!")
        break
    else:
        print("猜錯了!!")
    c=c+1
    print("猜錯第"+str(c)+"次!!")
    
    if c>4:
        
        print("猜錯第"+str(c)+"次!!"+","+"不能再猜了!!")
        break