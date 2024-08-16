import random # i used Visual studio code 
print("let's start the game!!!") #that l little introduction for the game
print("those are some names of heros from Mortal Kombat 11 you can use them if you want: \n[Sub-Zero,Scorpion,Raiden,Liu kang,Kang lao,Goro,Baraka,Shao kahn,Kano,Quan chi,Kitana,Reptile,Sindel,Jax,Mileena,Kenshi]")
print("______________________________________________________________________________________________________") 
#for the function name it asks for the names of heros.
def name():
    hero1=input("please type hero's 1 name:")
    while not(len(hero1)>1): #i used this while loop so that the hero name can't be empty 
        print("hero's name can't be empty")
        hero1=input("please type hero's 1 name:")
    hero2=input("please type hero's 2 name:")
    while not(len(hero2)>1): # i used this while loop so that the hero name can't be empty
        print("hero's name can't be empty")
        hero2=input("please type hero's 2 name:")
    while hero1==hero2: # i used the while loop so that the both names don't be the same 
        print(f"{hero1} is taken,please choose another name!") # this condition used to confirm that the both name are not the same 
        hero2=input("please type hero's 2 name:")
    print("______________________________________________________________________________________________________") 
    return hero1,hero2
#the function coin will determine which hero will start the fight with a percentage 50% 50% each. 
def coin(hero1,hero2):
    x=random.randint(0,1)
    if x==0:
        print(f"coin toss result: {hero1} start first!")
    else:
        print(f"coin toss result: {hero2} start first!")
    print("______________________________________________________________________________________________________") 
    return x
      
def health(hero1,hero2):  #function health it shows the health of each players in the start of the game. 
    h1=100
    h2=100
    z="I"
    print(f"{hero1:<59}{hero2}")
    print(f"HP[100]:{50*z:<40} HP[100]:{50*z}") 
    return h1,h2,z

def attack(z,x,hero1,hero2,h1,h2): #the attack function is the damage that has choose by the player to his opponent but by luck depends on the percentage(100-M) for the success and M for missing. 
    g=0
    s=0
    p=0
    while not(h1<=0 or h2<=0):    
        if x==0:
            print(f"{hero1} attacks!!")
            M=int(input("choose your attack magnitude between 1 and 50:"))
            while not(1<=M<=50):
                print("The attack magnitude must be between 1 and 50!!")
                M=int(input("choose your attack magnitude between 1 and 50:"))   
            y=M*"m"+(100-M)*"s"
            result=random.sample(y,1) #we multiplayed m(miss) with the attack magnitude and s(success) and then take randomly one character from the word y to know if the attack succeed or not with the a percentage of success 100-M and miss M 
            if result==['m']:
                print(f"ooopsy! {hero1} missed the attack!")# here in these case the health will stay the same and the attack won't effect it
                print(f"{hero1:<59}{hero2}")
                if len(str(h1))==1:
                    g=1
                else:
                    g=0           
                print(f'HP[{h1}]:{round(h1/2)*z:<51}{" "*g} HP[{h2}]:{round(h2/2)*z}') # writing the remaining health after each attack. 
            else:    
                h1=int(h1)
                h2=int(h2)-M
                if h2<=0: #if the health decrease under the zero with this condition will the health will be written 0 not -5 or -6
                    h2=0
                print(f"{hero1} hits {M} damage!!!")
                print(f"{hero1:<59}{hero2}")
                if len(str(h1))==1:
                    g=1
                else:
                    g=0         
                print(f'HP[{h1}]:{round(h1/2)*z:<51}{" "*g} HP[{h2}]:{round(h2/2)*z}') # writing the remaining health after each attack.
        else:
            print(f"{hero2} attacks!!")
            M=int(input("choose your attack magnitude between 1 and 50:"))
            while not(1<=M<=50): #with this loop the magnitude will be only between 1 and 50 
                print("The attack magnitude must be between 1 and 50!!")
                M=int(input("choose your attack magnitude between 1 and 50:"))   
            y=M*"m"+(100-M)*"s"
            result=random.sample(y,1)
            if result==['m']:
                print(f"ooopsy! {hero2} missed the attack!")# here in these case the health will stay the same and the attack won't effect it 
                h1=int(h1)
                h2=int(h2)
                print(f"{hero1:<59}{hero2}")
                if len(str(h1))==1:
                    g=1
                else:
                    g=0       
                print(f'HP[{h1}]:{round(h1/2)*z:<51}{" "*g} HP[{h2}]:{round(h2/2)*z}') # writing the remaining health after each attack.   
            else:    
                h1=int(h1)-M
                h2=int(h2)
                if h1<=0: #if the health decrease under the zero with this condition will the health will be written 0 not -5 or -6
                    h1=0
                print(f"{hero2} hits {M} damage!!!")
                print(f"{hero1:<59}{hero2}")
                if len(str(h1))==1:
                    g=1
                else:
                    g=0         
                print(f'HP[{h1}]:{round(h1/2)*z:<51}{" "*g} HP[{h2}]:{round(h2/2)*z}') # writing the remaining health after each attack.       
        x=abs(x-1) #to change the turn for each player with this equation x can be just 0 or 1 when x=0 its the turn of the 1st hero when x=1 its the turn of the second hero.     
    if (len(hero1)<10): #those condition used to make a good presentation for the result 
        s=10-len(hero1) 
    if (len(hero2)<10):    
        p=10-len(hero2)
    if h1<=0:
        print(f'####################################################################\n######################### {hero2}{" "*p}Wins!!! ########################\n####################################################################')  
    elif h2<=0:
        print(f'####################################################################\n######################### {hero1}{" "*s}Wins!!! ########################\n####################################################################')  
        # the result of the combat of the players.
                     
def respond(): # it asks the user if he wants to play again or not and it responds on the user depends on his answer.
    q=""
    rep=input("Do you want to play another round (Yes or No)? : ")
    q=rep.upper()   
    while not( q=="YES"or q=="NO"):
        rep=input("Do you want to play another round (Yes or No)? : ") 
        q=rep.upper()   
    if q=="NO":
        print("thanks for playing! see you again!")
    return q
                
hero1,hero2=name()        
q="YES"
while (q=="YES"): #asking for the response of the user if he wants to play again or not in form of while loop to make the game repeat when he answers with YES if NO the game will stop. 
    h1,h2,z=health(hero1,hero2)  
    x=coin(hero1,hero2)
    attack(z,x,hero1,hero2,h1,h2) 
    q=respond()
