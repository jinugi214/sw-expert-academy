T = int(input())

for t in range(1, T+1):
    text = input()
    word = []
    cnt = 0
    for i in text:
        if cnt > 0 and text[0] == i:
            length = len(word)
            if text[:length] == text[length:length+length]:
                print(f'#{t} {cnt}')
                break
        word.append(i)
        cnt += 1

