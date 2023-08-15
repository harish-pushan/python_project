import random
choices = ['r','p','s']
selection= random.choice(choices)

user_section= input("\n\nPlease pick a choice: 'r' or 's' or 'p' :")

if (selection==user_section):
    print("The match is a draw\n\n")

elif (user_section == 'r'and selection =='s') or (user_section=='s'and selection== 'p')or (user_section=='p'and selection=='r'):
    print("Congrats!!!, you have wooon :-)\n \n")
else:
    print('Sorry you have lost to the computer :-(\n\n')




