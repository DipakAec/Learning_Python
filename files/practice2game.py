from webbrowser import open_new


def game():
    return 88

score=game()

with open('hightscore.txt','r') as f:
    hightscore = int(f.read())

if hightscore<score:
    with open('hightscore.txt','w') as f:
        f.write(str(score))
