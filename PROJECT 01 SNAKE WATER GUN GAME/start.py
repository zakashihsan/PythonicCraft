import random
           #  snake, water, gun game program or 
             
            #  rock, paper, scissors
def gameWin(comp, you):
     if comp == you:
        return None
     elif comp == 's':
        if you == 'w':
           return False
        elif you == 'g':
           return True
        elif comp == 'w':
           if you == 'g':
              return False
           elif you == 's':
             return True
           elif comp == 'g':
            if you == 's':
             return False
            elif you == 'w':
             return True
      
print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
Rand = random.randint(1, 3)

if Rand == 1:
   comp = 's'
   
elif Rand == 2:
   comp = 'w'

elif Rand == 3:
   comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin (comp, you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
 
 print("The game is  tie!")
elif a:
 print("You win!")
else:
 print("You lose!")