+ # -*- coding: utf-8 -*-
#随机猜数字小游戏
import random
secret = random.randint(1,99)
guess = 0
tries = 0
- print "AHOY! I'm the dread Pirate Roberts, and I have a secret!"
- print "IT is number form 1 to 99. I'll give you 6 tries."
+ print "哈哈哈！我是恐怖海盗罗伯茨，我有一个秘密！"
+ print "这个数字是1到99.我会让你尝试6次。"
#可以猜6次
while guess != secret and tries < 6:
    guess = input("What's ")
    guess = input("你猜这个数字是? ")  
    if guess < secret:
        print "Too low, ye scurvy dog!"
        print "低啦,再高点儿!"
    elif guess > secret:
        print "Too high, landlubber!"
        print "高啦,再低点儿!"

    tries = tries + 1            # 猜的次数递增              

#最终显示结果
if guess == secret:                           \
    print "Avast! Ye got it!  Found my secret, ye did!"
    print "wo~ 你猜到了！你猜到了我的私密!"
else:
    print "No more guesses!  Better luck next time, matey!"
    print "The secret number was", secret
    print "次数用尽! 希望你下次能猜得更准，兄弟!"
    print "这次的私密数其实为：", secret