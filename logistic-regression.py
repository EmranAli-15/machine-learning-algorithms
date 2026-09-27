import math

x = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 4.0]
y = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1]


m = 0
c = 0
t_cost = float('inf')

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

n = len(x)

while True:
    cost = 0
    dm = 0
    dc = 0
    
    for i in range(n):
        z = m*x[i] + c
        prediction = sigmoid(z)
        
        eps = 1e-15
        prediction = max(min(prediction, 1 - eps), eps)
        
        cost += ( -y[i]*math.log(prediction)-(1-y[i])*math.log(1-prediction) )
        
        dm += (prediction - y[i])*x[i]
        dc += (prediction - y[i])
    
    m = m - 0.1*(dm/n)
    c = c - 0.1*(dc/n)
    
    if(abs(t_cost - cost/n) <= 0.00000001):
        break
    t_cost = cost/n


test_x = 100
result = sigmoid(m*test_x+c)
print("Pass" if result >= 0.5 else "Fail")
        
        