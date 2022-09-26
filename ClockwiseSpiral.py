'''
5
01 02 03 04 05
16 17 18 19 06
15 24 25 20 07
14 23 22 21 08
13 12 11 10 09

'''
l = [list(map(int,input().split())) for i in range(int(input()))]
top = 0
bottom = len(l)-1
left = 0
right = len(l[0])-1
dir = 0
while(top<=bottom and left<= right and dir<4):
    if(dir == 0):
        [print(l[top][i],end = " ") for i in range(left,right+1)]
        top+=1
    elif(dir == 1):
        [print(l[i][right],end = " ") for i in range(top,bottom)]
        right-=1
    elif(dir == 2):
        [print(l[bottom][i],end = " ") for i in range(right+1,left,-1)]
        bottom-=1
    elif(dir == 3):
        [print(l[i][left],end = " ") for i in range(bottom+1,top-1,-1)]
        left+=1
    dir= (dir+1)%4
