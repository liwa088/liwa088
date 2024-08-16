import datetime
import re
x={"ahmet":"1234","zeynep":"4444"} # a dictionary of the users
a={} # a dictionary the blocked users
z={"asparagus":[10,5],"broccoli":[15,6],"carrots":[18,7],"apples":[20,5],"banana":[10,8],"berries":[30,3],"eggs":[50,2],"mixed fruit juice":[0,8],"fish sticks":[25,12],"ice cream":[32,6],"apple juice":[40,7],"orange juice":[30,8],"grape juice":[10,9]}                       
t={"asparagus":[10,5],"broccoli":[15,6],"carrots":[18,7],"apples":[20,5],"banana":[10,8],"berries":[30,3],"eggs":[50,2],"mixed fruit juice":[0,8],"fish sticks":[25,12],"ice cream":[32,6],"apple juice":[40,7],"orange juice":[30,8],"grape juice":[10,9]}                       
basket=dict()# the basket of the user
name=""
amountuser=0            
def login(name,x,a):    # a login function for users and admin 
    print("****Welcome to Medipol Online Market****")
    print("please log in by providing your user credentials: ")
    name=""
    y={"admin":"qwerty"} # a dictionary for the administrator  
    fin=""
    np=0
    name=input("user name: ")
    password=input("password: ")
    while fin=="break" or not( name.lower() in y.keys() and str(password) in y.values()) and not( name.lower() in x.keys() and str(password) in x.values()):
        np+=1
        print("Your user name and/or password is not correct or may be blocked. Please try again!") # a loop her so that if he wrote the user name or the password wrong he can try again 
        name=input("user name: ")
        password=input("password: ")
        if np==2 and not( name.lower() in y.keys() and str(password) in y.values()) and not( name.lower() in x.keys() and str(password) in x.values()):
            print("Your account has been blocked. please contact the administrator.")
            for i,j in x.items():
                if i==name:
                    a[i]=j  # when the user wrote his password 3 times wrong his account will be blocked so i transfer it to the "a" dictionary
                    del x[i] # then delete it from the dictionary "x"
                    break   
                fin="break"
                break
            fin=login(name,x,a)    
    if np<2 and (( name.lower() in y.keys() and str(password) in y.values()) or (name.lower() in x.keys() and str(password) in x.values())):   
        print("Successfully logged in!")               
        fin=""
    return name,a,x,fin


def menu(name): # menu that will ask for some services for the  user or admin 
    chadmin=0
    choice=0
    print(f"Welcome, {name.lower()}! Please choose one of the following options by entering the corresponding menu number.")
    if name.lower()=="ahmet" or name.lower()=="zeynep":
        print("Please choose one of the following services:") # this services for users
        print("1. Search for a product")
        print("2. See Basket")
        print("3. Check Out")
        print("4. Logout")
        print("5. Exit")
        choice=int(input("Your Choice: ")) # here the choice of the user which service he want to choice
        while not 1<=choice<=5:
            print("your demand is not available!! try again.")
            choice=int(input("Your Choice: "))
            print("____________________________________________________________")
            print("____________________________________________________________")
    elif name.lower()=="admin":
        print("Please choose one of the following services:") #this services for admin
        print("1. Activate User Account")
        print("2. Deactivate User Account")
        print("3. Add User")
        print("4. Remove User")
        print("5. Logout")
        print("6. Exit")
        chadmin=int(input("Your Choice: ")) # here the choice of the admin which service he want to choice
        while not 1<=chadmin<=6:
            print("your demand is not available!! try again.")
            chadmin=int(input("Your Choice: "))
            print("____________________________________________________________")
            print("____________________________________________________________")   
    return chadmin,choice
def adminwork(x,a,menu): # the services of the admin is provided in this function 
    name="admin"
    chadmin,choice=menu(name)
    if chadmin==1: # when the choice=1 the admin can unblock any account
        if a=={}:
            print("there is no blocked account")
            adminwork(x,a,menu)                      
        elif a!={}:
            print(a)
            ans=input("which user you want to unblock:")
            for i,j in a.items():
                if i==ans:
                    paword=j
                    break
            del a[ans] # removing the user from the blocked dictionary 
            x.update({ans:paword})# and replace it in the x dictionary 
            print("the accounts has been unblocked")
            adminwork(x,a,menu) #after completing the admin will be returned to the menu
    elif chadmin==2: # when choice=2 the user can block a user w
        print("there is the list of our users who do you want to block!")
        print(x)
        ban=input("your choice: ") # the user that the admin want to ban 
        while not (ban in x.keys()):
            print("there is no one with that username")
            ban=input("your choice: ")
        for i,j in x.items():
            if ban==i:
                pasword=j
        del x[ban] # delete the user from the x dictionary 
        a.update({ban:pasword})# an place to the a dictionary 
        print("the account has been blocked successfully ")
        adminwork(x,a,menu) # after finishing the admin will return back to the sub-menu  
    elif chadmin==3:# here when choice of the admin equal to 3 he can add any user he want 
        username=input("what the name of the new use: ")
        password=input("enter his password: ")
        x.update({str(username):str(password)}) # and then add it to the x dictionary 
        print("the user has been added successfully")
        adminwork(x,a,menu) # after finishing the admin will return back to the sub-menu  
    elif chadmin==4: # when the choice=4 the admin can delete any account
        print("there is the list of our users who do you want to remove!")
        print(x)
        removeuser=input("your choice: ")
        while not (removeuser in x.keys()):# this loop willl repeat until the name will be match with the condition that the user name is in the dictionary X
            print("there is no one with that username")
            removeuser=input("your choice: ")             
        del x[str(removeuser)] #then delete that name here
        print("the account has been removed successfully")
        adminwork(x,a,menu)# after finishing the admin will return back to the sub-menu
    elif chadmin==5:# when the choice=5 the admin will logout
        name=""
        logout(a,x,base,login) 
    else: # when the choice=6 the admin will exit and the program will stop 
        exit()                
                
                                                
def choice1(name,main,basket,z,amountuser): #this function start when the use choice 1 in the sub-menu         
    for i,j in z.items():
        if j[0]==0:
            del z[i] #here when the amount of the item =0 the progam will not show it to the user
            break
    print("this is our stock what do you want to choice: ")
    print(z)
    order=input("What are you searching for ?: ")
    while not(str(order.lower()) in z.keys() or str(order.lower())=="juice"):# here a loop to make the user choose something inside the stock 
        order=input("Your search did not match any items. Please try something else (Enter 0 for main menu): ")   
        if str(order)=="0": # when here write 0 he will return back to the menu 
            main(name,menu,basket,z,x,a,amountuser,t)
                
    if str(order.lower())=="juice": 
        price=[]
        pro=[]
        amount=[]
        no=0
        for i,j in z.items():
            res=re.search("juice$",i) #here a condition the program will searchs for any word that end with juice  
            if res and int(j[0])>0: #then write it using this for loop 
                no+=1
                print(f"{no}.{i} {j[1]}$")
                pro.append(i)
                price.append(j[1])
                amount.append(j[0])
        print("____________________________________________________________")
        print("____________________________________________________________")

        additems=int(input("Please select which item you want to add to your basket (Enter 0 for main menu): ")) # the user need to choose the item he want from the items that the program provide       
        while not(0<=additems<=3):
            print("your demand is not available!! try again.")
            additems=int(input("Please select which item you want to add to your basket (Enter 0 for main menu): "))
        if additems==0: # if the choice is 0 so he will return to the menu 
            main(name,menu,basket,z,x,a,amountuser,t)

        elif additems==1: 
            amountuser=int(input(f"added {str(pro[0])}. Enter Amount: ")) # here the program will ask about the amount that the user want but if it more than the amount in the stock the program will ask again using the loop
            while not(1<=amountuser<=amount[0]):
                print("Sorry! The amount exceeds the limit, Please try again with smaller amount")
                amountuser=int(input("Amount (Enter 0 for main menu): "))
                if amountuser==0: #if the user write 0 he will retrun back to the menu
                    main(name,menu,basket,z,x,a,amountuser,t)

            else:
                basket[str(pro[0])]=[str(amountuser),str(price[0])] #if the condition is satisfied the basket will be fill by the itmes and the amount and the price of it 
                z.update({str(pro[0]):[int(amount[0])-int(amountuser),price[0]]}) # the program will update the stock amout and change it depends on the user amount
            print(f"added {str(pro[0])} into your Basket.")
            print("going back to the menu...")
            print("____________________________________________________________")
            print("____________________________________________________________")       
            main(name,menu,basket,z,x,a,amountuser,t) # finally he will return to the menu 
   
            return basket,z,amountuser       
        if additems==2:
            amountuser=int(input(f"added {str(pro[1])}. Enter Amount: ")) # here the program will ask about the amount that the user want but if it more than the amount in the stock the program will ask again using the loop
            while not(1<=amountuser<=amount[1]):
                print("Sorry! The amount exceeds the limit, Please try again with smaller amount")
                amountuser=int(input("Amount (Enter 0 for main menu): "))
                if amountuser==0: #if the user write 0 he will retrun back to the menu
                    main(name,menu,basket,z,x,a,amountuser,t)

            else:
                basket[str(pro[1])]=[str(amountuser),str(price[1])]# if the condition is satisfied the basket will be fill by the itmes and the amount and the price of it
                z.update({str(pro[1]):[int(amount[1])-int(amountuser),price[1]]})# the program will update the stock amout and change it depends on the user amount
            print(f"added {str(pro[1])} into your Basket.")
            print("going back to the menu...")
            print("____________________________________________________________")
            print("____________________________________________________________")
            main(name,menu,basket,z,x,a,amountuser,t) # finally he will return to the menu
              
            return basket,z,amountuser
        if additems==3:
            amountuser=int(input(f"added {str(pro[2])}. Enter Amount: ")) # here the program will ask about the amount that the user want but if it more than the amount in the stock the program will ask again using the loop
            while not(1<=amountuser<=amount[2]):
                print("Sorry! The amount exceeds the limit, Please try again with smaller amount")
                amountuser=int(input("Amount (Enter 0 for main menu): "))
                if amountuser==0:#if the user write 0 he will retrun back to the menu
                    main(name,menu,basket,z,x,a,amountuser,t)

            else:
                basket[str(pro[2])]=[str(amountuser),str(price[2])]# if the condition is satisfied the basket will be fill by the itmes and the amount and the price of it
                z.update({str(pro[2]):[int(amount[2])-int(amountuser),price[2]]}) # the program will update the stock amout and change it depends on the user amount                                       
            print(f"added {str(pro[2])} into your Basket.")
            print("going back to the menu...")
            print("____________________________________________________________")
            print("____________________________________________________________")
            main(name,menu,basket,z,x,a,amountuser,t) # finally he will return to the menu
       
            return basket,z,amountuser    
    elif str(order.lower()) in z.keys():# here the order can be anything 
        price=[]
        pro=[]
        amount=[]
        print(f"1.{order.lower()}")
        for i,j in z.items():
            if i==order.lower():
                pro.append(i)
                price.append(j[1])
                amount.append(j[0])             
        print("____________________________________________________________")
        print("____________________________________________________________")             
        additems=int(input("Please select which item you want to add to your basket (Enter 0 for main menu): "))# the user need to choose the item he want from the items that the program provide
        while not(0<=additems<=1):
            print("Your search did not match any items. Please try something else")
            additems=int(input("Please select which item you want to add to your basket (Enter 0 for main menu): "))   
        if additems==0:#if the user write 0 he will retrun back to the menu
            main(name,menu,basket,z,x,a,amountuser,t)

        else:
            amountuser=int(input(f"added {order.lower()}. Enter Amount: "))# here the program will ask about the amount that the user want but if it more than the amount in the stock the program will ask again using the loop
            while not(1<=amountuser<=amount[0]):
                print("Sorry! The amount exceeds the limit, Please try again with smaller amount")
                amountuser=int(input("Amount (Enter 0 for main menu): "))
                if amountuser==0:#if the user write 0 he will retrun back to the menu
                    main(menu,basket,z,x,a,amountuser,t)

            else:
                basket[str(pro[0])]=[amountuser,price[0]]# if the condition is satisfied the basket will be fill by the itmes and the amount and the price of it
                z.update({str(pro[0]):[int(amount[0])-int(amountuser),price[0]]})# the program will update the stock amout and change it depends on the user amount
            print(f"added {str(pro[0])} into your Basket.")
            print("going back to the menu...")
            print("____________________________________________________________")
            print("____________________________________________________________")
            main(name,menu,basket,z,x,a,amountuser,t)# finally he will return to the menu

            return basket,z,amountuser
    
    return basket,z,amountuser

        
def seebasket(name,basket,z,checkout,main,amountuser,x,t): # this function is for choice 2 when the user want to use the items of his basket 
    print("Your basket contains:")
    num=0
    tot=0
    if basket=={}:
        print("your basket is empty and the total price of items is 0$") #the program will tell the user that his basket is empty if he want to see his basket 
        print("total=0$")
    else:
        for i,j in basket.items(): # a loop to present the items and calculate the total
            num+=1
            tot=tot+(int(j[1])*int(j[0]))
            print(f"{num}.{i}={j[1]}$ amount={j[0]} total={int(j[0])*int(j[1])}$")
        print(f"total={tot}$")                      
    print("Please choose an option:")#then the program will open a new menu for the seebasket function
    print("1.Update amount")
    print("2.Remove an item")
    print("3.Check out")
    print("4.Go back to main menu")
    chbasket=int(input("Your selection: "))
    while not (1<=chbasket<=4): # a condition so that our choice will be between 1 and 4
        print("your demand is not available!! try again.")
        chbasket=int(input("Your selection: "))
    if chbasket==1: # if choice =1 the user can update any amount off his basket 
        price=[]
        pro=[]
        amount=[]
        amountz=[]
        itemch=int(input("Please select which item to change its amount: "))
        while not (1<=itemch<=len(basket)): # this loop used so that the user could choose just an item inside the basket 
            print("Your search did not match any items. Please try something else")
            itemch=int(input("Please select which item to change its amount: ")) 
        for x,w in basket.items():
            for i,j in t.items():
                if i==x:
                    pro.append(i)
                    price.append(w[1])
                    amount.append(w[0])
                    amountz.append(j[0])      # here the amount of the stock      
        newamount=int(input("Please type the new amount: "))
        while not(1<=newamount<=(int(amountz[itemch-1]))): # this condition used so that the amount can't be more than the amount of the stock 
            print("Sorry! The amount exceeds the limit, Please try again with smaller amount")
            newamount=int(input("Please type the new amount: "))
        basket[str(pro[itemch-1])]=[newamount,price[itemch-1]]# if the condition is satisfied the basket will be fill by the itmes and the amount and the price of it
        z.update({str(pro[itemch-1]):[int(amountz[itemch-1])+int(amountuser)-int(newamount),price[itemch-1]]})# the program will update the stock amonut and change it depends on the user amount
        amountuser=newamount   
        seebasket(name,basket,z,checkout,main,amountuser,x,t) # finally he will return to the menu
        return basket,amountuser   
    elif chbasket==2: # here if the user choose 2 he can remove any item he want 
        price=[]
        pro=[]
        amount=[]
        amountz=[]
        remitem=int(input("Please select which item you want to remove: "))
        while not (1<=remitem<=len(basket)): # this loop used so that the user could choose just an item inside the basket 
            print("Your search did not match any items. Please try something else")        
        for x,w in basket.items():
            for i,j in t.items():
                if i==x:
                    pro.append(i)
                    price.append(w[1])
                    amount.append(w[0])
                    amountz.append(j[0])
        del basket[str(pro[remitem-1])] # the program will delete the chosen item from the basket 
        z.update({str(pro[remitem-1]):[int(amountz[remitem-1]),price[remitem-1]]}) # the program will update the stock amonut and change it depends on the user amount               
        seebasket(name,basket,z,checkout,main,amountuser,x,t) # finally he will return to the menu
        return basket,amountuser
    
    elif chbasket==3: # if he choose 3 then he will checkout and return to the main menu 
        checkout(name,basket,main)    
    elif chbasket==4:
        main(name,menu,basket,z,x,a,amountuser,t) # if he choose 4 he will return back to the main menu

def checkout(name,basket,main):  # the program will print the receipt of the user .
    print("Processing your receipt...")
    print("******* Medipol Online Market ********")
    print("**************************************")            
    print("444 8 544")
    print("medipol.edu.tr")
    print("___________________________________")
    num=0
    tot=0
    if basket=={}: #here if the user basket is empty he will show it empty 
        print("your basket is empty and the total price of items is 0$")
        print("___________________________________")
        print("total=0$")
        print("___________________________________")
        ch = datetime.datetime.now() # i improt the time module so that the program will provide me th real time after checking out 
        print(ch)
        print("Thank You for using our Market!")
        print("___________________________________")
        print("___________________________________")
        main(name,menu,basket,z,x,a,amountuser,t) #then finally it will return to the main menu 

    else:
        for i,j in basket.items():
            num+=1
            tot=tot+(int(j[1])*int(j[0]))
            print(f"{num}.{i}={j[1]}$ amount={j[0]}") # the program will print the basket items and the amounts then the total price
        print("___________________________________")
        print(f"total={tot}$") 
        print("___________________________________")
        ch = datetime.datetime.now() # i improt the time module so that the program will provide me th real time after checking out
        print(ch)
        print("___________________________________")
        print("Thank You for using our Market!")
        print("___________________________________")
        print("___________________________________")
        main(name,menu,basket,z,x,a,amountuser,t)#then finally it will return to the main menu 

def logout(a,x,base,login): # the logout function will make the user or the admin logout and to to the login section 
    name=""
    name,a,x,fin=login(name,x,a)
    base(name,main,adminwork,a,x,t) 
      
def main(name,menu,basket,z,x,a,amountuser,t):    # the main function that take the choice and respond depends the choice
        chadmin,choice=menu(name) # menu that will ask for some services for the  user or admin 
        if choice==1: 
            basket,z,amountuser=choice1(name,main,basket,z,amountuser) #this function start when the use choice 1 in the sub-menu 
        elif choice==2:
            basket,amountuser=seebasket(name,basket,z,checkout,main,amountuser,x,t) # this function is for choice 2 when the user want to use the items of his basket
        elif choice==3:
            checkout(name,basket,main) # the program will print the receipt of the user
        elif choice==4:
            logout(a,x,base,login) # the logout function will make the user or the admin logout and to to the login section
        elif choice==5:
            print("Thank you for buying from us and see you next time.")
            exit() # the exit function it stops the program
 
name,a,x,fin=login(name,x,a)  # a login function for users and admin
while fin=="break":
    name,a,x,fin=login(name,x,a)                
def base(name,main,adminwork,a,x,t):    # this function is the base function of the code it will take the name 
    if name=="admin": # if name is admin so the program will compile the admin part 
        adminwork(x,a,menu)# the services of the admin is provided in this function
    elif name in x.keys(): # if name any other user in our data the program will provide the user part 
        main(name,menu,basket,z,x,a,amountuser,t)
    return name,x,a
name,x,a=base(name,main,adminwork,a,x,t)    
