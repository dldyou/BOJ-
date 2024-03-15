import numpy as np
import hashlib

# 추첨 인원수
winner_num = 5
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

# 참가자가 각 div에서 푼 최대 문제수 (통합)
participants = {}
for participant in info:
    user = participant.split()[1]
    corrects = participant.count('/') - participant.count('--') - 1
    if user in participants:
        participants[user] = max(participants[user], corrects)
    else: participants[user] = corrects
    
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

# 정보 출력
print(f'랜덤 시드: {seed_string}')
print(f'참가자: {list(participants.keys())}')
print(f'맞은 문제 개수: {list(participants.values())}')
print(f'확률: {winner_percent}')

# 당첨자
winner = np.random.choice(list(participants.keys()), winner_num, replace = False, p = winner_percent) \
    if winner_num < len(participants) else list(participants.keys())
print(f'\n당첨자: {winner}')
