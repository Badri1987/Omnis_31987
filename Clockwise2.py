'''
04 05 06 07
03 14 15 08
02 13 16 09
01 12 11 10

5
05 06 07 08 09
04 19 20 21 10
03 18 25 22 11
02 17 24 23 12
01 16 15 14 13
'''
l = [list(map(int,input().split())) for i in range(int(input()))]
top = 0
bottom = len(l)-1
left = 0
right = len(l[0])-1
dir = 0
while(top<=bottom and left<=right and dir<4):
    if (dir == 0):
        [print(l[i][left],end = " ") for i in range(bottom,top-1,-1)]
        left+=1
    elif (dir == 1):
        [print(l[top][i],end = " ") for i in range(left,right+1)]
        top+=1
    elif(dir == 2):
        [print(l[i][right],end =" ") for i in range(top,bottom)]
        right-=1
    elif(dir == 3):
        [print(l[bottom][i],end = " ") for i in range(right,left-1,-1)]
        bottom-=1

    dir=(dir+1)%4