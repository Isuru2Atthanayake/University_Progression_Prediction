#part2
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID:20200265       /w1810007  
  
# Date:  11/12/2020

#num_p= pass credit
#num_f=failcredit
#num_d=deffercredit
list_1=[0,20,40,60,80,100,120]#list in range 0,20,40,60,80,100,120 
total=0
print("=====This is a student version of the progression outcomes======\n")
print("---------------------Guide lines------------------------------\n")
print("1:Enter your credits for the programme..................")
print("2:Total of your credits should be equal to 120 .........")
print("3:Enter valid integers only.............................\n")
def check_val(p):#definition function
    if p not in list_1:
        p=int(input("Out of range"))
    return p
try:
    print('------------------------------------------------------')#prints a verticle line.     

    num_p = int(input("Please enter your credits at pass:  "))#Enter the credits at pass.
    num_p=check_val(num_p)#checks num_p in the definition list,
    
    num_d= int(input("Please enter your credits at defer:  "))#Enter the credits at defer.
    num_d=check_val(num_d)#checks num_d in the definition list,
    
    num_f= int(input("Please enter your credits at fail:   "))#Enter the credits at fail.
    num_f=check_val(num_f)#checks num_f in the definition list,

    total=num_p+num_d+num_f#total of the 3 credits
    
    if total !=120:
        print("Total incorrect")
    else:
        
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

except ValueError:
    print("Integer required")#if a credit input is in the wrong data type.
    

    
