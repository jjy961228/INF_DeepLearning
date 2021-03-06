#%% 1-14) 
# =============================================================================
# Vector Operation(벡터 연산)
# 성질) elements-wise operation : 같은 차원에있는 요소끼리 연산 가능
# =============================================================================
# x1 과 x2 / y1,y2 / z1, z2
# 는 각각 같은 차원에 있는 것이다
x1 , y1, z1 = 1, 2, 3 #하나의 벡터로 생각
x2 , y2, z2 = 4, 5, 6

x3, y3, z3 = x1 + x2 , y1 + y2 , z1 + z2
x4, y4, z4 = x1 - x2 , y1 - y2 , z1 - z2
x5, y5, z5 = x1 * x2 , y1 * y2 , z1 * z2

print("벡터의 덧샘: " , x3, y3, z3)
print("벡터의 뺄셈: ", x4, y4, z4)
print("빅터의 곰셈(하다마드곱): ", x5, y5, z5) 

#%% 1-15)

# =============================================================================
# Scalar-Vector Operation(스칼라-벡터 연산)
# 성질) (scalar) *,+,- (Vector) 할 수 있다 
# =============================================================================
a = 10
x1, y1, z1 = 1, 2, 3

x2, y2, z2 = a+x1, a+y1, a+z1
x3, y3, z3 = a-x1, a-y1, a-z1
x4, y4, z4 = a*x1, a*y1, a*z1

print("scalar+V: " , x2, y2, z2)
print("scalar-V: " , x3, y3, z3)
print("scalar*V: " , x4, y4, z4)

#%% 1-16)
# =============================================================================
# Vector Norm : 벡터의 크기를 의미한다 (즉, 직선의 길이)
# 성질) 직선의 길이는 피타고라스 정리를 이용해서 구할 수 있다
#       n차원Vector의 모든원소의 제곱 합에 루트씌운것 
# =============================================================================
x, y, z = 1, 2, 3

#3차원상에서 norm값 
vector_norm = (1**2 + 2**2 + 3**2)**0.5
print("vector_norm: " , vector_norm)

#%%
# =============================================================================
# Unit Vector(U) : 벡터의크기(norm)를 1로 만들어주는 Vector
# 성질) 크기가5였다면 -> UnitVetor -> 방향이 같고, 크기가 1인벡터로 바뀐다
# =============================================================================
x, y, z = 1, 2, 3

norm = (x**2 + y**2 + z**2)**0.5

#UnitVector 만들어주기(기존의 벡터를 norm으로 나눠주기)
x_unitVector = x / norm
y_unitVector = y / norm
z_unitVector = z / norm
print("x의 unitVector: " , x_unitVector)
print("y의 unitVector: " , y_unitVector)
print("x의 unitVector: " , z_unitVector)

#unitVector를 이용해 norm 값 구하기
# 즉, 벡터의 크기(직선의길이) 구하기
# -> norm이 1로 바뀌었다
new_norm = (x_unitVector**2 + y_unitVector**2 + z_unitVector**2)**0.5
print("norm: ", new_norm)



#%% <정리>
# =============================================================================
# norm 이란? 직선의 길이 -> 피타고라스 정리 생각
# ex)
# (a,b,c) 가 있을때,
# norm = (a**2 + b**2,c**2)**0.5
# 
# unitVector 란? norm을 1로 만들어주는 벡터
#                 즉, 직선의 길이를 1로 만들어주는 벡터
# ex)
# (a,b,c) 가 있을때,
#  a_unitVector = a / ((a**2 + b**2 + c**2)**0.5)
#               = a / norm
# 
# norm = {(a_unitVector**2) + (b_unitVector**2) + (c_unitVector**2)}**0.5
# 즉, unitVector에 의해 norm 값이 1이되었다
# =============================================================================








