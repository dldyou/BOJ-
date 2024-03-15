import numpy as np
import hashlib

# 추첨 인원수
winner_num = 5
# 문제 수
problems_num = 5
# BOJ 연습란을 텍스트로 긁어오면 됩니다 (랭킹, 아이디, A, B, C, ... 맨 윗줄 제외하고)
info = """

"""
# 랜덤 시드
mod = 4294967296 # 2^32
seed_string = "Hello, AlKon!"
random_seed = int.from_bytes(hashlib.sha256(seed_string.encode()).digest(), 'big') % mod
np.random.seed(random_seed)

# 정보 처리
delimiter = (5 + problems_num * 3)
info = info.split()
participants_num = len(info) // delimiter # 참가자 수
participants_list = [''] * participants_num # 참가자 명단
correct_problems = [0] * participants_num # 각 참가자가 푼 문제 개수

for i in range(participants_num):
    participants_list[i] = info[i * delimiter + 1]
    for j in range(problems_num):
        if info[i * delimiter + 1 + j * 3] != '--':
            correct_problems[i] += 1

# 추첨 명단 제외 리스트 
except_list = []
for except_user in except_list:
    try:
        idx = participants_list.index(except_user)
        participants_list.pop(idx)
        correct_problems.pop(idx)
        participants_num -= 1
    except:
        pass
    
# 추첨 확률 설정
winner_percent = [0] * participants_num
correct_problems_sum = sum(correct_problems)

for i in range(participants_num):
    winner_percent[i] = correct_problems[i] / correct_problems_sum

print(f'랜덤 시드: {seed_string}')
print(f'참가자: {participants_list}')
print(f'맞은 문제 개수: {correct_problems}')
print(f'확률: {winner_percent}')

# 당첨자
winner = np.random.choice(participants_list, winner_num, replace = False, p = winner_percent) \
    if winner_num < participants_num else participants_list
print(f'당첨자: {winner}')