ram = [2,4,6]
rom = [16,32,64]
camera = [8,8,12]
display_size = [5.0,5.2,5.5]

features = [ram, rom, camera, display_size]
price = [10000,12500,15000]

total_data = len(price)
total_feature = len(features)

cost = 0
weights = [0]*(total_feature+1)


while True:
    features_weight = [0]*(total_feature+1)
    
    total_cost = 0
    for i in range(total_data):    
        hw=weights[0]
        
        for j in range(total_feature):
            hy = weights[j+1]*features[j][i]
            hw += hy
        
        features_weight[0] += (hw - price[i])
        for p in range(total_feature):
            features_weight[p+1] += ((hw - price[i])*features[p][i])
            
        
        total_cost += (hw-price[i])**2
    
    mean_cost = total_cost/total_data
    mean_features_weight = [w/total_data for w in features_weight]

    if abs(mean_cost-cost)<=0.0001:
        break
    
    cost = mean_cost
    
    for i in range(total_feature+1):
        weights[i] = weights[i] - 0.001*mean_features_weight[i]


ra=4
ro=32
ca=8
di=5.2
print(f"New phone price for ram={ra}, rom={ro}, camera={ca}, display={di} is = {weights[0] + weights[1]*ra + weights[2]*ro + weights[3]*ca + weights[4]*di} TK")