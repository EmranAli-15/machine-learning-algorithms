import math


training_data = [
#   outlook    temp    routine  wear used/unused(not listed for original data)
    ["sunny", "cold", "indoor", "no", 0],
    ["sunny", "warm", "outdoor", "no", 0],
    ["cloudy", "warm", "indoor", "no", 0],
    ["sunny", "warm", "indoor", "no", 0],
    ["cloudy", "cold", "indoor", "yes", 0],
    ["cloudy", "cold", "outdoor", "yes", 0],
    ["sunny", "cold", "outdoor", "yes", 0]
]

parameter = {
    "outlook": {
        "features": ["sunny", "cloudy"],
        "index": 0
    },
    "temperature": {
        "features": ["cold", "warm"],
        "index": 1
    },
    "routine": {
        "features" : ["indoor", "outdoor"],
        "index": 2
    }
}


class Node:
    def __init__(self, name=None, value=None, left=None, right=None):
        value = value
        left = left
        right = right
        name = name


class Tree:
    def build(self, table_data):
        if not parameter:
            return

        # calculating parent data entropy
        #--------------------------------

        total_yes = 0
        total_no = 0
        total_data = 0

        for data in table_data:
            if(data[4] == 1):
                continue

            if data[3] == "yes":
                total_yes+=1
            else:
                total_no+=1
            total_data+=1

        parent_entropy = (-((total_yes/total_data)*math.log2(total_yes/total_data))-((total_no/total_data)*math.log2(total_no/total_data)))

        print(parent_entropy)
        
        # calculating parent data entropy
        #--------------------------------





        # calculating available features entropy
        #---------------------------------------
        
        new_total_data = 0
        for data in training_data:
            if data[4] == 0:
                new_total_data+=1

        features_gain = {}

        for key, value in parameter.items():
            entropy = 0
            
            for feature in value["features"]:
                feature_yes = 0
                feature_no = 0
                
                for data in training_data:
                    if data[value["index"]] == feature and data[3] == "yes" and data[4] == 0:
                        feature_yes+=1
                    elif data[value["index"]] == feature and data[3] == "no" and data[4] == 0:
                        feature_no+=1
                print(feature_yes, feature_no)
                
                # calculating entropy with individual feature -- facing issue here
                ####
                ####
                ####
                entropy += ((feature_yes+feature_no)/new_total_data) * (-((feature_yes/(feature_yes+feature_no))*math.log2(feature_yes/(feature_yes+feature_no)))-((feature_no/(feature_yes+feature_no))*math.log2(feature_no/(feature_yes+feature_no))))

            features_gain[key] = parent_entropy-entropy

        print(features_gain)
        # calculating available features entropy
        #---------------------------------------

ob = Tree()
ob.build(training_data)