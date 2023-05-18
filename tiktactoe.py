def check(x,y,t,TikTacToe):
    if TikTacToe[x][y]==0:
        TikTacToe[x][y]=t
    else:
        print("Already the position is filled choose the right position")
        TikTacToe1(t)
def TikTacToe1(t):
    print("Enter the right values")
    x,y=map(int,input().split())
    check(x,y,t,TikTacToe)
def won(a):
    if (TikTacToe[0].count(a)==3 or TikTacToe[1].count(a)==3 or TikTacToe[2].count(a)==3 or (TikTacToe[0][0]==a and TikTacToe[1][0]==a and TikTacToe[2][0]==a) or (TikTacToe[0][1]==a and TikTacToe[1][1]==a and TikTacToe[2][1]==a) or (TikTacToe[0][2]==a and TikTacToe[1][2]==a and TikTacToe[2][2]==a) or (TikTacToe[0][0]==a and TikTacToe[1][1]==a and TikTacToe[2][2]==a) or (TikTacToe[0][2]==a and TikTacToe[1][1]==a and TikTacToe[2][0]==a)):
        return 1
    return 0
def dcheck(TikTacToe):
    if TikTacToe[0].count(0)==0 and TikTacToe[1].count(0)==0 and TikTacToe[2].count(0)==0:
        return 1
    return 0
def TikTacToe2(TikTacToe):
    print("Enter player X")
    x,y=map(int,input().split())
    check(x,y,'X',TikTacToe)
    if won('X'):
        print("Player A won")
        return
        
    if dcheck(TikTacToe):
        print("Draw")
        return
    print("Enter player O")
    x,y=map(int,input().split())
    check(x,y,'O',TikTacToe)
    if won('O'):
        print("Player B won")
        return
    TikTacToe2(TikTacToe)
TikTacToe=[[0,0,0],[0,0,0],[0,0,0]]
TikTacToe2(TikTacToe)
    
    
    
    
