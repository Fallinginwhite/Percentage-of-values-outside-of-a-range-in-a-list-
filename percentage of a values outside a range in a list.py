import math
temperatures = [5,4,3,2,-1,0]
count = 0 
for i in range(0,len(temperatures)):
    if temperatures[i] < 0 or temperatures[i] > 5:
          count +=1
        

percentage = count / len(temperatures) *100
percentage = percentage // 1
int(percentage)
print(int(percentage), "% is out of the range")
