#input name
#get a ancrypted message
#a casino game
#a dictionary


name_allowed=("NEEL","BIMAL","SUBHAM","AKASH")


name = input("Please enter your name - ").upper()

x=True
if name in name_allowed[0]:
    print(name + " bhaiya welcome :)")
    
    message=("dnkjiuqahweyuruiyseopifkpokkm,xcvcnnmzbnvzhgadvaqieuweorjpoifbnjhfdebovjb").upper()

    print(message[5:6],message[13:14],message[ 7:8]+message[ 9:10]+message[-6:-5]+message[ 17:18]+message[-4:-3]+message[28:29]+message[-6:-5])
    
elif name in name_allowed[1]:
    print(name + " made this one for u")
    
elif name in name_allowed[2]:
    print(name + " is a friend of your")
    
elif name in name_allowed[3]:
    print(name + " is a friend of mine")
    
else :
    print("sorry, i dont know this name")
    

    
    


print ("now we gonna play a game. ")




def game():
    import random
    
    x=[random.randint(0,3) for i in range(4)]
    print(x)
    if x == [3,3,3,3]:
        print('win')
    else :
        print('lose')
        

command=""

started=False

while True:
    command = input(">>>  ").lower()
    if command == "start":
         game()
         
   
    elif command =="try again":
        
        if not started:
            
            game()
        else :
            print('start the game first')
        
         
    
    elif command == "help":
        print('''
              "start" = "to start"
              "try again" = "to try again"
              "quit" = "to exit"
              
              if all numbers are same you win 
              good luck
             
             '''         )

    elif command =="quit":
        break
    
    else:
        print("sorry i don't understand that")


