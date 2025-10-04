print("Welcome to the Patter Generator and Number Analyzer")

print("1: Generate a pattern ")
print("2: Analye a range of number ")
print("3: Exit")

choice = int(input("Enter your choice: "))

match choice:
        case 1: 
               rows = int(input("enter the number for pattern :"))
               for i in range(1, rows + 1):
                 print('*' * i)
                
        case 2 :
                val1 = int(input("enter the start of the range :"))
                val2 = int(input("enter the end of the range :"))  
                sum = 0 
                for i in range(val1 , val2 + 1):   
                      if i % 2 == 0:
                        print("num is",i, "even")
                      else :
                        print("num is",i,"odd")
                      sum += i
                print("sum of all number is",sum)   
        case 3 :
            print("Exiting the program..Goodbye!!")
