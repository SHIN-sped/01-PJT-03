import sys

sys.stdin = open("_직사각형길이찾기.txt")

	T = int(input())
 
for tc in range(1,1+T):
 
    number = list(map(int,input().split()))
 
    number.sort()
 
    if number[0] != number[1]:
        print('#{} {}'.format(tc,number[0]))
    else:
        print('#{} {}'.format(tc,number[2]))
