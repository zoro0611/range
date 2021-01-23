# range範圍
# python 內建功能: 清單產生器
import random

range(5) # [0, 1, 2, 3, 4]
range(2, 10, 3) # [2, 5, 8] =>從2開始，每次增加3，不能超過10
range(10, 3, -2) # [10, 8, 6, 4] =>從10開始，每次減少2，不能低於3



for i in range(100):
	r = random.randint(1, 1000)
	print("這是第", i +1, "次產生隨機數", r,)


