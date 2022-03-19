#part1
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID:20200265   / w1810007      
  
# Date:  11/12/2020

print("=====This is a Student version of the progression ======\n")
print("---------------------Guide lines------------------------------\n")
print("1:Enter your credits for the programme..................")
print('------------------------------------------------------\n')#prints a verticle line.     
num_p = int(input("Please enter your credits at pass:  "))#Enter the credits at pass.

num_d= int(input("Please enter your credits at defer:  "))#Enter the credits at defer.

num_f= int(input("Please enter your credits at fail:   "))#Enter the credits at fail.

if num_p==120:
    print("progress")
    print('------------------------------------------------------')#prints a verticle line. 
               
elif num_p==100:
    print("progress(module trailer)")
    print('------------------------------------------------------')#prints a verticle line.      
               
elif num_f==120 or num_f==100 or num_f==80:
    print("Exclude")
    print('------------------------------------------------------')#prints a verticle line.     
              
else:
    print("Do not progress - module retriever")
    print('------------------------------------------------------')#prints a verticle line.     
            

    
