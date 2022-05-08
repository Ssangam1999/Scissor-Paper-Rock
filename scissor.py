import random
def game(you,comp):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            return True
        elif you=='r':
                return False
    elif comp=='p':
        if you=='s':
            return False
        elif you=='r':
                return True
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
             return False          

    


print(" Computer turn :choose 1 for scissor 2 for paper 3 for rock")
randno=random.randint(1,3)
if randno==1:
    comp = 's'
elif randno==2:
    comp = 'p'
elif randno==3:
    comp = 'r'
you=input("Your turn: select scissor(s),paper(p),,rock(r)")
game(you,comp)