import random

# problem = [("p1", "답"), ("p2", "답2"),("p3", "답3"),("p4", "답4")]

import pandas as pd
import numpy as np
data = pd.read_csv('TestLists.csv', encoding ='cp949')
problem = data.to_numpy()

print ("몇 개의 문제를 풀 것인가요? ", len(problem), "이하의 숫자만 입력하세요." )
count = int(input().strip())
score = 0
skip = 0
wrong_answers = []


while count > len(problem):
    print(len(problem), "이하의 숫자만 입력하세요.")
    count = int(input().strip())

qqq = len(problem)-count

while len(problem) != qqq:
    row_index = random.randint(0, len(problem) -1)
    question = problem[row_index]
    print(question[0])
    answer = input()
    

    while answer.strip() != question[1]:
        
        print("땡! 다시 입력하세요. pass를 원하시면 pass 라고 입력해주세요.")
            
        answer = input() 
            
        if answer == "pass" :
            wrong_answers = wrong_answers + [(question[0],question[1])]
            print(wrong_answers)
            skip=skip+1
            break
        
    if answer.strip() == question[1]:
        score = score + 1
        
        #print("다음문제")

    problem = np.delete(problem, row_index, 0)
    
    # print(problem)

print(score)
print(count)
print ("최종점수는",(score/count)*100,"점 입니다.", "정답:",score,"Pass:",skip)

# 추가해야될것 
# 1. 틀린문제의 정답 보여주기! -> 해결
# 2. 영->한, 한->영 모드
# 3. I am = I'm, I would like to = I'd like to => 정답처리

# In the future,
# 1. 일상, 비즈니스, 시사 등 분야와 레벨 선택
# 2. 영->한 번역시 비슷한 것 정답처리 (자연어처리?)
# 3. 자주 틀리는 문제 



# for i in range(len(problem)):
#     questionList = random.choice(problem)
#     print(problem[i][0])
#     answer = input()

        
#     while answer != problem[i][1]:
#         print("땡! 다시 입력하세요.")
#         answer = input()
#     print("정답")

    




