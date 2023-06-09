import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
SYMBOLS_QUANTITY = {"A":2, "B":4, "C":6, "D":8}
SYMBOLS_WEIGHT = {"A":5, "B":4, "C":3, "D":2}

def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <=  lines <= MAX_LINES :
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for key, value in symbols.items():
        for _ in range(value):
            all_symbols.append(key)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value1 = random.choice(current_symbols)
            current_symbols.remove(value1)
            column.append(value1)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    #print(balance, lines)
    slots = get_slot_machine_spin(ROWS, COLS, SYMBOLS_QUANTITY)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOLS_WEIGHT)
    print(f"You won ${winnings}.")
    if len(winning_lines) > 0:
        print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is : ${balance}")
        if balance == 0:
            res2 = input("Press enter to deposit more or q to quit: ")
            if res2 == 'q':
                break
            else:
                balance = deposit()
                print(f"Current Balance is : ${balance}")
        response = input("Press enter to spin or q to quit: ")
        if response == 'q':
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()