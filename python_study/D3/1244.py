T = int(input())

def dfs(si, cnt):
    global ans
    if cnt == n:
        val = int(''.join(nums))
        if ans < val:
            ans = val
        return

    # 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.
    else:
        for i in range(si, len(nums)):
            for j in range(i+1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                val = int(''.join(nums))
                if (val, cnt) not in used:
                    used.add((val, cnt))
                    dfs(i, cnt+1)
                nums[i], nums[j] = nums[j], nums[i]

for t in range(1, T + 1):
    input1, input2 = input().split()
    nums = list(input1)
    n = int(input2)

    used = set()
    # 횟수만큼 자리바꿈으로 교환하고 가장 큰수를 출력하기
    ans = 0
    dfs(0, 0)
    print(f'#{t} {ans}')
