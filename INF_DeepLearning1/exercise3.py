#%% 1-18)
# Dot Product : (벡터의 각 element의 곱)의 합
x1, y1, z1 = 1, 2, 3
x2, y2, z2 = 4, 5, 6

dot_product = (x1*x2) + (y1*y2) + (z1*z2)
print(dot_product)

#%% 1-19)
# Euclidean distance (유클리드 거리) == L2 distance 라고도 부른다
# 정의) n차원 공간에서의 두 점사이의 거리 -> 피타고라스 정리 이용
x1, y1, z1 = 1, 2, 3
x2, y2, z1 = 4, 5, 6

e_distance = (x1-x2)**2 + (y1-y2)**2 + (z1-x2)**2
e_distance **= 0.5 # e_distance = edistance**0.5

print(e_distance)

#%% 1-20)
# =============================================================================
# Squared Error(에러의 제곱) : 내가 예측한 값이 얼마나 정확한가 ? -> 두 점사이의 거리로 구한다
# 즉,(예측값-실제값)**2
# =============================================================================
#실제값
y1 , y2 , y3 = 10, 20, 30

#pred: 예측값
pred1 , pred2 , pred3 = 10, 25, 40 

#Squared Error
s_error1 = (pred1-y1)**2
s_error2 = (pred2-y2)**2
s_error3 = (pred3-y3)**2

#0, 25, 100 -> 정확, 5만큼 차이, 10만큼 차이
print(s_error1, s_error2, s_error3)

#%%
# =============================================================================
# Mean Squared Error(에러 제곱의 평균) 
# -> 즉, (예측값-실제값)**2 의 평균
# =============================================================================
x1 , y1, z1 = 10, 20, 30

pred1 ,pred2, pred3 = 10, 25, 40

#Squared Error
s_error1 = (pred1 - x1)**2
s_error2 = (pred2 - y1)**2
s_error3 = (pred3 - z1)**2

#Mean Squeard Error
mse = (s_error1 + s_error2 + s_error3) / 3
print("Mean_Squared_Error: " , mse)





