N=(int)(input())
cnt=0
if N==1000:
    N-=1
    
if N<100:
    cnt=N
       
else :
    cnt=99
    while N>99:
        n=N
        
        il=n%10
        n//=10
        
        sip=n%10
        n//=10
         
        baek=n%10
        
        if il-sip==sip-baek:
            cnt+=1
        N-=1
            
        
print('%d' %cnt)
