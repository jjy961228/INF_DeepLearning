#%% 1-10)
# =============================================================================
#  Mean Subtraction : 평균빼기
#  x := x-mean
#  정의 )모든 변수에서 평균을 빼준다
# =============================================================================
score1 , score2, score3 = 10, 20, 30
student_n = 3

#평균
score_mean = (score1 + score2 + score3) / student_n
print(score_mean)

# x := x-mean
score1 -= score_mean
score2 -= score_mean
score3 -= score_mean

# x := x-mean 한후 , 평균으로 나눠주면 0이 나온다 !
score_newMean = (score1 + score2 + score3) / score_mean
print(score_newMean)

#%% 1-11)
# =============================================================================
# mean_of_square , square_of_mean
# 제곱의 평균 , 평균의 제곱
#    E(X**2)      E(X)**2
# =============================================================================
score1 , score2, score3 = 10, 20, 30
student_n = 3

score_mean = (score1 + score2 + score3) / 3

#제곱의 평균
mean_of_square = (score1**2 + score2**2 + score3**2) / student_n

#평균의 제곱
square_of_mean = score_mean**2

print("평균의 제곱 :" , square_of_mean)
print("제곱의 평균 :" , mean_of_square)

#%% 1-12)
# =============================================================================
# 분산(Variance) 과 표준편차(Standard deviation)
# V(X) = E(X**2) - E(X)**2 
# std = V(X)**0.5   #0.5제곱은 루트와 같다
# =============================================================================
score1 , score2, score3 = 10, 20, 30
student_n = 3

score_mean = (score1 + score2 + score3) / 3

#E(X**2)
mean_of_square = (score1**2 + score2**2 + score3**2) / student_n
#E(X)**2
square_of_mean = score_mean**2

#Varinace
score_variance = mean_of_square - square_of_mean
print("varinace:" ,score_variance)

#Standard diviation(std)
score_std = score_variance**0.5
print("std:" , score_std)

#%% 1-13)
# =============================================================================
# Standardization(표준화)
# x := (x-mean) / (variance)**0.5
# =============================================================================
score1 , score2, score3 = 10, 20, 30
student_n = 3

score_mean = (score1 + score2 + score3) / 3

mean_of_square = (score1**2 + score2**2 + score3**2) / student_n
square_of_mean = (score_mean)**2

#variance
score_variance = mean_of_square -square_of_mean
print(score_variance)

#standard diviation
score_std = score_variance**0.5

#stadardization
score1_stadardization = (score1 - score_mean) / score_std
score2_stadardization = (score2 - score_mean) / score_std
score3_stadardization = (score3 - score_mean) / score_std

print("socre1_stadardization :" ,score1_stadardization)
print("score2_stadardization : ",score2_stadardization)
print("score3_stadardization: ",score3_stadardization)

#stadardization: 
#    Mean subtraction 을하고, 평균을 구하면 0이 나온다
#   따라서, 모든 것에 Mean subtraction을 하고, 평균을구하면 0이 나온다
score_mean = (score1 + score2 + score3) / 3
print(score_mean)







 












