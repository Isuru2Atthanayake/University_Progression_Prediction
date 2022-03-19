#part3 (staff version with histogram)
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID:20200265         / w1810007 
  
# Date:  11/12/2020

#num_p= pass credit
#num_f=failcredit
#num_d=deffercredit
list_1=[0,20,40,60,80,100,120]#list in range 0,20,40,60,80,100,120 
total=0
Progress_count=0
module_retriever_count=0
module_trailer_count=0
Exclude_count=0
tot=0
print("=====This is a staff version of the progression outcomes======\n")
print("---------------------Guide lines------------------------------\n")
print("1:Enter your credits for the programme..................")
print("2:Total of your credits should be equal to 120 .........")
print("3:Enter valid integers only.............................\n")

def check_val(p):#definition function
    if p not in list_1:
        p=int(input("Out of range"))
    return p#returns the def function
            
while True :
        q = input("Enter any key to continue or else enter 'q' to quit the program:")#this is a option for the user either quit or continue.
        if q=='q':
              break#breaks the while loop
        try:
            print('------------------------------------------------------')#prints a verticle line.     
            print("staff version with histogram \n")
            num_p = int(input("Please enter your credits at pass:  "))#Enter the credits at pass.
            num_p=check_val(num_p)#checks num_p in the definition list,
            
            num_d= int(input("Please enter your credits at defer:  "))#Enter the credits at defer.
            num_d=check_val(num_d)#checks num_d in the definition list,
            
            num_f= int(input("Please enter your credits at fail:   "))#Enter the credits at fail.
            num_f=check_val(num_f)#checks num_f in the definition list,

            total=num_p+num_d+num_f#total of the 3 credits

            
            
            if total !=120:#if the total of 3 credits not equal to 120 prints as "Total incorrect"
                print("Total incorrect")
            else:
                        if num_p==120:#if pass credit equals 120 then print progress
                            print("progress")
                            print('------------------------------------------------------')#prints a verticle line. 
                            Progress_count=Progress_count+1#takes a count
                            
                        elif num_p==100:#if pass credit equals 100 then print "progress(module trailer)"
                            print("progress(module trailer)")
                            print('------------------------------------------------------')#prints a verticle line.      
                            module_trailer_count=module_trailer_count+1
                            
                        elif num_f==120 or num_f==100 or num_f==80:#if pass credit equals 120 or 100 or 80 then print Exclude
                            print("Exclude")
                            print("------------------------------------------------------")#prints a verticle line.     
                            Exclude_count=Exclude_count+1
                        else:
                            print("Do not progress - module retriever")
                            print('------------------------------------------------------')#prints a verticle line.
                            module_retriever_count=module_retriever_count+1

                             
        except ValueError:
                print("Integer required")#if a credit input is the wrong data type.
  
print("------------------------------------------------------")
print("Horizontal Histogram")
print("progress:",Progress_count,"*"*Progress_count)
print("Trailer:",module_trailer_count,"*"*module_trailer_count)
print("Retriever:",module_retriever_count,"*"*module_retriever_count)
print("Exclude:",Exclude_count,"*"*Exclude_count)
print(Progress_count+module_trailer_count+module_retriever_count+Exclude_count,"outcomes in total.")
print("------------------------------------------------------")
