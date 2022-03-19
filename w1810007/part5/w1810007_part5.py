# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID:20200265          /w1810007 
  
# Date:  11/12/2020

pass_credit=[0,20,40,60,80,100,120]#list for pass credits
fail=[20,40,60,80,100,120]#list for fail credits
x=120
total=0
Progress_count=0
module_retriever_count=0
module_trailer_count=0
Exclude_count=0

if x in pass_credit:
        Progress_count=Progress_count+1#count of progress
        print("Progress")#prints progress
        
for pass_credit in range(120,99,-20):#range between 120 to 100 and reduces by 20
        module_trailer_count=module_trailer_count+1#count of progress module trailer
        print("Progress (module trailer)")
        
for fail in range(0,61,20):#range between 0 to 60
        module_retriever_count=module_retriever_count+1
        print("Do not Progress-module retriever")
        
for fail in range(80,121,20):#range between 80 and 120 has a gap of 20
        Exclude_count=Exclude_count+1
        print("Exclude")
        #Historgram
print("Progress:",  Progress_count,"*"*Progress_count)
print("Trailing:",  module_trailer_count,"*"*module_trailer_count)
print("retriever:", module_retriever_count,"*"*module_retriever_count)
print("Excluded:",  Exclude_count,"*"*Exclude_count)
print(Progress_count+module_trailer_count+module_retriever_count+Exclude_count,"Out comes in total.")#prints the total of outcomes.

