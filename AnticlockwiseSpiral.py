'''
5
05 04 03 02 01  00 01 02 03 04
06 19 18 17 16  10 11 12 13 14
07 20 25 24 15  20 21 22 23 24
08 21 22 23 14  30 31 32 33 34
09 10 11 12 13  40 41 42 43 44
'''
m = [list(map(int,input().split())) for i in range(int(input()))]
top = 0
bottom = len(m)-1
left = 0
right = len(m[0])-1
dir = 0
while(top<=bottom and left<=right and dir<4):
    if (dir == 0):
        [print(m[top][i],end = " ")  for i in range(right,left-1,-1)]
        top+=1
    elif(dir==1):
        [print(m[i][left],end = " ") for i in range(top,bottom+1)]
        left+=1
    elif(dir==2):
        [print(m[bottom][i],end =" ") for i in range(left,right+1)]
        bottom-=1
    elif(dir==3):
        [print(m[i][right],end =" ") for i in range(bottom,top-1,-1)]
        right-=1

    dir=(dir+1)%4
