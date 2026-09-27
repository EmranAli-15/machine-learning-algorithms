x = [6,8,12,14,18]
y = [350,775,1150,1395,1675]
ln = len(x)

cost = 0
m=0
c=0

while True:
    t_cost=0
    t_m=0
    t_c=0
    for i in range(ln):
        hy = m*x[i]+c
        
        t_cost += (hy-y[i])**2
        
        t_m += (hy-y[i])*x[i]
        t_c += (hy-y[i])
    
    mean_cost = t_cost/ln
    mean_m = t_m/ln
    mean_c = t_c/ln
    
    m = m-0.01*mean_m
    c = c-0.01*mean_c
    
    if abs(mean_cost-cost) <= 0.001:
        break
    cost = mean_cost

print(f"Prediction for 17 inch = {m*17+c}")