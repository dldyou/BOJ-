import numpy as np
import hashlib

# 추첨 인원수
winner_num = 10
# BOJ 연습란을 텍스트로 긁어오면 됩니다 (랭킹, 아이디, A, B, C, ... 맨 윗줄 제외하고)
info = """
"""
info = info.splitlines(keepends = True)
if info[0] == "\n": info.pop(0)

# 랜덤 시드
mod = 4294967296 # 2^32
seed_string = "Hello, AlKon!"
random_seed = int.from_bytes(hashlib.sha256(seed_string.encode()).digest(), 'big') % mod
np.random.seed(random_seed)

participants = {}
for participant in info:
    participant = participant.split('\t')
    user = participant[1]
    corrects = int(participant[-1].split(' / ')[0])
    if user in participants:
        participants[user] = max(participants[user], corrects + 3)
    else: participants[user] = corrects + 3
    
# 추첨 명단 제외 리스트 
except_list = []
for except_user in except_list:
    try:
        participants.pop(except_user)
    except:
        pass
    
# 추첨 확률 설정
winner_percent = [0] * len(participants)
correct_problems_sum = sum(participants.values())

for i, corrects in enumerate(list(participants.values())):
    winner_percent[i] = corrects / correct_problems_sum

print(f'랜덤 시드: {seed_string}')
print(f'{len(participants)}명 {list(participants.keys())}')
# print(f'맞은 문제 개수: {list(participants.values())}')
# print(f'확률: {winner_percent}')

# 당첨자
winner = np.random.choice(list(participants.keys()), winner_num, replace = False, p = winner_percent) \
    if winner_num < len(participants) else list(participants.keys())
winner.sort()
print(f'당첨자: {winner}')
