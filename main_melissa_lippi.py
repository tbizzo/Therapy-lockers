import random

def gioca():
    try:
        m = int(input("Select 1 for rock, 2 for scissor, 3 for paper:\n"))
    except ValueError:
        print("Your move is not valid...")
        return gioca()

    r = random.randint(1, 3)  # generates 1, 2 or 3

    # User's move
    if m == 1:
        print("(ง •_•)🤜 ", end='')
    elif m == 2:
        print("(ง •_•)✌️ ", end='')
    elif m == 3:
        print("(ง •_•)🖐 ", end='')
    else:
        print("Your move is not valid...")
        return gioca()

    # Computer's move
    if r == 1:
        print("🤛 (•̀_•́ผ)")
    elif r == 2:
        print("✌️ (•̀_•́ผ)")
    elif r == 3:
        print("🖐 (•̀_•́ผ)")

    # Determine the result
    if m == r:
        print("\nIt's a tie!!")
    elif (m == 1 and r == 2) or (m == 2 and r == 3) or (m == 3 and r == 1):
        print("\nYou won!")
    else:
        print("\nYou lost!")

    g = input("\nDo you want to play again? y/n:\n").strip().lower()
    if g == 'y':
        gioca()
    else:
        print("Thank you for playing, you are beautiful!")

if __name__ == "__main__":
    random.seed()
    gioca()
