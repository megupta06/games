#part1.1

def  get_checkin_bags(bag_weights,min_weight, max_weight ):
    
    bag= []
    for i in bag_weights:
        if i <= max_weight and i >= min_weight:
            bag += [i]
    return bag
    

'''
bag_weights = input("bag_weights= ")
min_weight = int(input("min_weight= "))
max_weight = int(input("max_weight= "))

bag_weights_new = get_checkin_bags ( bag_weights,min_weight, max_weight)           
print ("Returns: " , (bag_weights_new))
'''


'''
#part1.3

def print_statistics (data):
    count_0=0
    count_neg=0
    count_pos=0
    for i in range(len(data)):
        Maximum= max(data)
        Minimum= min(data)
        Mean= sum(data)/ len(data)
        if data[i]==0 :
            count +=1
        elif data[i]<0:
            count_neg +=1
        elif data[i]>0:
            count_pos +=1
    print("Maximum: ", Maximum)
    print("Minimum: ", Minimum)
    print("Mean:", Mean)
    print("Number of occurrences of Zero:", count_0)
    print("Number of negative numbers:", count_neg)
    print("Number of positive numbers:",count_pos)
            
                      
        
#part1.4
    
    def print_pattern (n):
    for index in range(1,n+1):
        print("* " *index)

'''












