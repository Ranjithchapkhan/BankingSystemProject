print(120*"=")

customersname=["Shiva","Ramu","Ranjith","Priya","sindhu","madhu"]
customerspin=["1234","5678","9966","0123","6301","7998"]
customerbalances=["2000","2300","10000","30000","18000","1500"]
balance=0
deposit=0
withdrawl=0
i=0
counter_1=1
counter_2=6

while True:
    print(120*"*")
    print(47*"-","WELCOME TO SIB BANK",52*"-")
    print(120*"*")
    print("\n")
    print("=> 1.Account Opening <=")
    print("=> 2.Amount Withdrawl <=")
    print("=> 3. Deposit Amount <=")
    print("=> 4.Customer's list & balances <=")
    print("=> 5.Exit <=")
    print(120*"*")
    
    option=input("Select any option from above menu:")
    if option=="1":
        print("option 1 is selected by the customer")
        N=eval(input("Number of customers:"))
        i=i+N
        if i>6:
           print("\n")
           print("Customer registration limit is execeded")
           i=i-N
        else:
            while counter_1<=i:
                Name=input("Enter your Full Name:")
                customersname.append(Name)
                Pin=str(input("Enter Pin of your choice:"))
                customerspin.append(Pin)
                balance=0
                deposit=int(input("Enter amount to Deposit:"))
                balance=balance+deposit
                customerbalances.append(balance)
                print("\nName:",end=" ")
                print(customersname[counter_2])
                print("pin:",end=" ")
                print(customerspin[counter_2])
                print("Balance:",end=" ")
                print(customerbalances[counter_2],end=" ")
                print("/-Rs")
                counter_1=counter_1+1
                counter_2=counter_2+1
                print("\nYour name is added to our bank system")
                print("Your pin is added to our bank system")
                print("Your balance is added to our bank system")
            
                print(80*"-","Your Account is created successfully",80*"-")
                print("\n")
            
                print("Your Name is available on our customer's list")
                print(customersname)
                print("NOTE! please Remember your Pin & Don't share to anyone")
      
        Mainmenu=print("Press ENTER key to go back to Mainmenu to perform another action or to Exit") 
    
             
    elif option=="2":
        j=0
        print("option 2 is selected by the coustmer ")
          
        while j<1:
            k=-1
            name=input("Enter your name:")    
            pin=input("Enter your pin:")
        
            while k<len(customersname)-1:
                k=k+1
            
                if name==customersname[k]:
                   if pin==customerspin[k]:
                       j=j+1
                       print("Your current balance:",end=" ")
                       print(customerbalances[k],end=" ")
                       print("/-Rs\n")
                       balance=(customerbalances[k])
               
                       Withdrawl=int(input("Enter amount to withdraw:"))
    
     
                       if Withdrawl > 1000:
                           print("No sufficient balance!! ,Please enter less amount")
                       else:
                            balance=1000-Withdrawl
                            print("\n")
                            print(47*"-","WITHDRAWL SUCCESSFULL",50*"-")
                            customerbalances[k]=balance
                            print("your remaining balance:",balance,end="")
                            print("/-Rs\n\n")
            if j<1:
               print("Your Name and Pin doesn't match")    
               break   
        Mainmenu=print("Press ENTER key to go back to Mainmenu to perform another action or to Exit")     
        
        
        
    elif option=="3":
        n=0
        print("option 3 is selected by the customer ")
          
        while n<1:
            k=-1
            name=input("Enter your name:")    
            pin=input("Enter your pin:")
        
            while k<len(customersname)-1:
                k=k+1
            
                if name==customersname[k]:
                   if pin==customerspin[k]:
                       n=n+1
                       print("Your current balance:",end=" ")
                       print(customerbalances[k],end=" ")
                       print("/-Rs")
                       balance=(customerbalances[k])
               
                       deposit=eval(input("Enter amount to Deposit:"))
                       balance=1000+deposit
                       customerbalances[k]=balance
                       print("\n")
                       print(47*"-","DEPOSIT SUCCESSFULL",52*"-") 
                       print("Your new balance:",balance,end="")
                       print("/-Rs\n\n")
            if n<1:
               print("Your Name and Pin doesn't match")    
               break   
        Mainmenu=print("Press ENTER key to go back to Mainmenu to perform another action or to Exit")
        
    elif option=="4":
        print("option 4 is selected by the customer")
        k=0
        print("customer name list and balances are mentioned below:")
        print("\n")
        while k<= len(customersname)-1:
            print("==> Coustmer :",customersname)   
            print("==> Balance :",customerbalances[k],end=" ") 
            print("/-Rs")
            print("\n")
            k=k+1       
        Mainmenu=print("Press ENTER key to go back to Mainmenu to perform another action or to Exit")
        
    elif option=="5":
        print("option 5 selected by the coustmer")   
        print("Thank You for selecting our bank")
        print("\n")
        print(100*"=","VISIT AGAIN",100*"")
        Mainmenu=print("Press ENTER key to go back to Mainmenu to perform another action or to Exit")
        
    else:
      print("invalid option selected")
      print("Please try again")
      Mainmenu=print("Press ENTER key to go back to Mainmenu to perform another action or to Exit")
        