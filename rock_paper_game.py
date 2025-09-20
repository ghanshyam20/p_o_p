# we are going to crate a scissor rok paper game 

# rules
# rock>scissors
# scissor>paper
# paper>rock
# 
# 
#  
#  
import random
scissors=r''' ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
  '''


rock=r'''              \
 _____         \
| | | |/\       \
|_|_|_|\ \       \
|        /
\_______/            (  ( ) ) ( )  )
 \______\           ( ( ( ( )  )  ) )
 \       \         ( ( )) ) (   ) ( ( )
  \       \        ( (__.-.___.-.__) )
   \       \        /---._.---._.--- \
    \       \       \||   '  \'    ||/
     \       \       |||     _)   |||
      \       \       ||||///\\\||||
       \       \_____/ ||||\__/||||\___
        \             \ |||||||||| /   \
         \             \  ||||||  /     \
          \_____

'''


paper=r''' _ __   _____      _____ _ __   __ _ _ __   ___ _ __ 
| '_ \ / _ \ \ /\ / / __| '_ \ / _` | '_ \ / _ \ '__|
| | | |  __/\ V  V /\__ \ |_) | (_| | |_) |  __/ |   
|_| |_|\___| \_/\_/ |___/ .__/ \__,_| .__/ \___|_|   
                        | |         | |              
                        |_|         |_| 

                        '''


game_images=[rock,paper,scissors]
# user choice

user_choice=int(input("what do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n"))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])



computer_choice=random.randint(0,2)
print("computer choise:")
print(game_images[computer_choice])

if user_choice>=3 or user_choice<0:

    print("you typed an invalid number , you lose")
elif user_choice==0 and computer_choice==2:
    print("You win !")
elif computer_choice==0 and user_choice==2:
    print("you loose")

elif computer_choice>user_choice:
    print("you loose")

elif user_choice>computer_choice:
    print("You win !")


elif user_choice==user_choice:
    print("its draw")

