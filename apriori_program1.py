import itertools 
c1={}
l1={}
unique_itmes={}
l1copy={}
min_support=2
min_conf=66
dataset={'T1':['I1','I2','I5'],
         'T2':['I2','I4'],
         'T3':['I2','I3'],
         'T4':['I1','I2','I4'],
         'T5':['I1','I3'],
         'T6':['I2','I3'],
         'T7':['I1','I3'],
         'T8':['I1','I2','I3','I5'],
         'T9':['I1','I2','I3']} 

print("------>Dataset<------")
for i in dataset:
        for j in dataset[i]:
            if j not in c1:
                c1[(j)]=1
            else:   
                c1[(j)]+=1
        print(dataset[i])   


print("\n-->Candidate Set C1 : ")
print(c1)
unique_items=c1


def remove(vect,k):
        if len(tuple(set(vect)))==k:
            return tuple(set(vect))
        return -1

def L_generate(l1):
    l1copy=l1.copy()
    l1.clear()
    for i in c1:
        if c1[i]>=min_support:
            l1[i]=c1[i]    
    return l1copy
            
def generate_k_plus_1(k,c1):   
        c1.clear()
        count=count1=0
        for i in l1:
            for j in l1:
                if count<=count1:
                    count+=1
                else:
                    if k==2:
                            key=remove((i,j),k)
                    else:
                            key=remove((i+j),k)
                    if key==-1:
                        continue;
                    else:
                        c1[key]=0

            count1+=1;
            count=0

def proning(kremove,c1):
        c2=c1.copy()
        for k in c1: 
            subset=itertools.combinations(k,kremove)
            for j in subset:
                flag=0
                for i in l1:
                    if i==j:
                        flag=1
                        break;
                if(flag==0):
                    c2.pop(k)
                    break;
    
        c1=c2.copy()
        return c1
               
            
    
        
def find_frequency(c1):
    for j in c1:   
            for i in dataset:
                       if(all(elem in dataset[i] for elem in list(j))):
                            c1[j]+=1

def findSupport(divisor):  
            count=0
            for i in dataset:
                       if(all(elem in dataset[i] for elem in list(divisor))):
                            count+=1
            return count
        
        
L_generate(l1)
print("-->L1 : ")
print(l1)    
len1=len(unique_items.keys())
for i in range(1,len1):
        generate_k_plus_1(i+1,c1)
        if(i!=1):
            c1=proning(i,c1)
        find_frequency(c1)
        l1copy=L_generate(l1)
        if(len(l1.keys())!=0):
                 print("\n")
                 print("-->Candidate Set C"+str(i+1)+" : ")
                 print(c1) 
                
                 print("-->L"+str(i+1)+" : ")
                 print(l1)
        else:
            break;
        

print("\n\n---> final frequent item set are <--------")
print(l1copy)


print("\n\nfinal association rule are:")
rule=tuple()
for dividend in l1copy:
     for j in range(1,len(dividend)):
            temp=itertools.combinations(dividend,j)
            for divisor in temp:
                if ((l1copy[dividend]/findSupport(divisor))*100)>min_conf:
                    temp1=itertools.combinations(dividend,len(dividend)-j)
                    for k in temp1:
                                if set(divisor).issubset(k) or set(k).issubset(divisor):
                                       continue
                                else:
                                        print(str(divisor)+"-->"+str(k)+"  with confidence:"+str((l1copy[dividend]/findSupport(divisor))*100))
                                        break;






