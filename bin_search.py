
# 1.2
#import math
#
#bin_search = math.log(240000,2) #240000から二分探索で任意の数字を特定する際の計算量
#print(bin_search)
#二分探索ではlog 2 n 個の要素を探す必要がある
#ex) log 2 1024 = 10 だから二分方ならば10個の要素を探す必要がある
#ソート済みの場合の話


def binary_search(list, item):
    low  = 0
    high = len(list) - 1 #a_list = [1,2,3] ; len(a_list) #=> 3 ; a_list[0] #=> 1

    while low <= high: #lowからhighまでloopする
        mid   = (high + low) // 2 #2の整数で割った商が帰ってくる
        print("mid = ", mid)
        guess = list[mid] #第一引数で与えられたlistの真ん中の値
        if guess == item: # 
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


#練習問題
#1.1
import math
print(math.log(128,2)) #128の要素から二分探索で任意の数字を特定する際の計算量
    #=> 7

#1.2
import math
print(math.log(256,2)) #256の要素から二分探索で任意の数字を特定する際の計算量
    #=> 8
