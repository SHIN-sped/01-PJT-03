import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for i in range(T):
    test_number = int(input())
    scores = list(map(int, input().split()))
    mode = 0

    count_dic = {}
    for i in scores:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1

    max_count = 0
    for key, value in count_dic.items():
        if max_count < value:  # 4
            max_count = value
            mode = key
        elif max_count == value:  # 5
            if mode < key:
                mode = key

    print('#{} {}'.format(test_number, mode))
