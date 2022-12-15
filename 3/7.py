S = input()

exp = len(S)-1
res = 0
if exp > 0:
    for i in range(2**exp):
        bits = format(i, 'b').zfill(exp)
        idx = 1
        tmp = S[0]
        for j in bits:
            if j == '1':
                res += int(tmp)
                tmp = S[idx]
            else:
                tmp += S[idx]
            idx += 1
        res += int(tmp)
else:
    res = int(S)
print(res)


#####################
# 答えのC++をchatgptで変換したコード
S = input()
N = len(S)

# N-1 箇所の隙間に「+」を入れるかどうかをすべて試す
res = 0
for bit in range(1 << (N-1)): # +を入れる場所を決める
    # tmp：「+」と「+」との間の値を表す変数
    tmp = 0
    for i in range(N-1):
        tmp *= 10
        tmp += ord(S[i]) - ord('0')

        # 「+」を挿入するとき、答えに tmp を加算して、tmp を 0 に初期化
        if bit & (1 << i):
            res += tmp
            tmp = 0

    # 最後の「+」から残りの部分を答えに加算
    tmp *= 10
    tmp += ord(S[-1]) - ord('0')
    res += tmp

print(res)
