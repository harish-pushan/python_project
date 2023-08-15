import random
#for simplicity if user wants to bet on one line its the top line 
#and so on and so forth

MAXLINES=3
MAXBET= 100
MINBET= 1


ROWS= 3
COLS=3



symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(colums,lines,bet,values):
    winnings =0
    winning_lines=[]
    for line in range(lines):
        symbol= colums[0][line]
        for colum in colums:
            symbol_to_check= colum[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines  





def get_slot_machine_spin(rows,cols,symbols):
    all_symbol=[]
    for symbol,symbol_count in symbols.items():
       for _ in range(symbol_count):
           all_symbol.append(symbol)
#I dont knw how i created this logic it kinda worked dont ask me how it worked 
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols= all_symbol[:]
        for _ in range(rows):
            value= random.choice(all_symbol)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns    



def print_slot_machine(columns):
#len(columns[0]) states that there is atleast one colums in a the variable
    for row in range(len(columns[0])):
        #to print the first value in the row 
        for i,column in enumerate (columns):
            #enumerate is used to loop over a list or tuple
            if i != len(columns)-1:
                #this exist to not let the "|" on the end of the 3rd column
                print(column[row],end=" | ")
#the | is there to seperate the columns 
            else:
                print(column[row],end="")
        print()
#because i killed and masacerd the logic in the get_slot_machine_spin
#and had my colums kinda repsent as rows now i gotta transpose them like a matrix
#i need a lot of training i hate myself






def deposit():
    while True:
        amount = input("Please enter the amount to be deposited :$")
        if amount.isdigit():
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid number :")
            
    return amount


def get_Number_of_lines():
    while True:
        lines = input("Please enter the lines to place the bet on (1-"+ str(MAXLINES)+")? ")
        if lines.isdigit():
            lines= int(lines)
            if 1 <= lines<= MAXLINES :
                break
            else:
                print("ENTER A VALID NUMBER OF LINES")
        else:
            print("Please enter a valid number :")
            
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? :$")
        if amount.isdigit():
            amount= int(amount)
            if MINBET<= amount <= MAXBET:
                break
            else:
                print(f"Bet must between ${MINBET}-${MAXBET}.")
        else:
            print("Please enter a valid number :")
            
    return amount

def spin(balance):
    lines = get_Number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>balance:
            print("You do not enough balance to make this bet.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots= get_slot_machine_spin(COLS,ROWS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines )
    return winnings - total_bet

def main():        
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer= input("press enter to spin (q to quit)")
        if answer=="q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
    
main()





