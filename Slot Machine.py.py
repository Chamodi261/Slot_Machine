import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbol counts and values
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

# Function to check winnings based on the slot machine spin
def check_winnings(columns, lines, bet, values):
    """
    Check if there are any winning combinations in the slot machine spin.

    Parameters:
    - columns: List of columns representing the slot machine spin.
    - lines: Number of lines bet on.
    - bet: Bet amount on each line.
    - values: Dictionary containing symbol values.

    Returns:
    - Tuple containing total winnings and a list of winning lines.
    """
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(lines + 1)

    return winnings, winnings_lines

# Function to generate a slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a slot machine spin.

    Parameters:
    - rows: Number of rows in the slot machine.
    - cols: Number of columns in the slot machine.
    - symbols: Dictionary containing symbol counts.

    Returns:
    - List of columns representing the slot machine spin.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

# Function to print the slot machine spin
def print_slot_machine(columns):
    """
    Print the slot machine spin.

    Parameters:
    - columns: List of columns representing the slot machine spin.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Function to handle player deposit
def deposit():
    """
    Get the initial deposit amount from the player.

    Returns:
    - Initial deposit amount.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

# Function to get the number of lines to bet on
def get_num_of_lines():
    """
    Get the number of lines to bet on from the player.

    Returns:
    - Number of lines to bet on.
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? " )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

# Function to get the bet amount on each line
def get_bet():
    """
    Get the bet amount on each line from the player.

    Returns:
    - Bet amount on each line.
    """
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount

# Function to perform a slot machine spin
def spin(balance):
    """
    Perform a slot machine spin and calculate winnings.

    Parameters:
    - balance: Current player balance.

    Returns:
    - Net change in balance after the spin.
    """
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance} ")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You Won ${winnings}!!!")
    print(f"You Won On Lines:", *winning_lines)
    return winnings - total_bet

# Main game loop
def main():
    balance = deposit()
    while True:
        print(f"Current Balance is: ${balance}")
        answer = input("Press Enter to Play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

# Run the game
main()
