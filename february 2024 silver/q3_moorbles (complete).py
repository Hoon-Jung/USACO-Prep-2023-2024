cases = int(input())
for _ in range(cases):
    marbles, moves, K = map(int, input().split())
    responses = []
    for i in range(moves):
        choices = [float("inf"), float("inf")]
        for pmoves in map(int, input().split()):
            if pmoves % 2 == 0:
                choices[0] = min(choices[0], pmoves)
                choices[1] = min(choices[1], -pmoves)
            else:
                choices[0] = min(choices[0], -pmoves)
                choices[1] = min(choices[1], pmoves)
        responses.append(choices)
    min_poss = [0] * (moves+1)
    for m in range(moves):
        min_poss[-1 - (m + 1)] = min(0, max(responses[-(m+1)]) + min_poss[-(m+1)])
    if min_poss[0] + marbles <= 0:
        print(-1)
        continue
    ans = ""
    for n in range(moves):
        if marbles + responses[n][0] > -min_poss[n+1]:
            ans += "Even "
            marbles += responses[n][0]
        else:
            ans += "Odd "
            marbles += responses[n][1]
    print(ans[:-1])   
    



# def solve():
#     N, M, K = map(int, input().split())

#     changes = []
#     for _ in range(M):
#         change_for_turn = [float("inf")] * 2
#         for a in map(int, input().split()):
#             parity = a & 1
#             change_for_turn[parity] = min(change_for_turn[parity], a)
#             change_for_turn[parity ^ 1] = min(change_for_turn[parity ^ 1], -a)
#         changes.append(change_for_turn)
#     min_psum = [0] * (M + 1)
#     for t in reversed(range(M)):
#         min_psum[t] = min(0, max(changes[t]) + min_psum[t + 1])
#     if N + min_psum[0] <= 0:
#         print(-1)
#         return
#     ans = []
#     for t in range(M):
#         p = 1 if (N + changes[t][0] + min_psum[t + 1] <= 0) else 0
#         ans.append(p)
#         N += changes[t][p]
#     print(" ".join([["Even", "Odd"][p] for p in ans]))


# T = int(input())
# for _ in range(T):
#     solve()