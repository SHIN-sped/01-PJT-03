import sys

sys.stdin = open("_문자열의거울상.txt")


T = int(input())
 
for test_case in range(1, T+1):
    case = input()
    text = ''
    for i in case[::-1]:
        if i == 'b':
            text += 'd'
        elif i == 'd':
            text += 'b'
        elif i == 'p':
            text +='q'
        else:
            text += 'p'
    print('#{}'.format(test_case), text)