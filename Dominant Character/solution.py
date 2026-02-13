#length of the smallest substring
#length of the sub string is atleast 2
#'a' occurs strictly more times in this substring than 'b'
#'a' occurs strictly more times in this substring than 'c'

#output is the length of smallest substring satisfing the above condition

def slidingwindow(s,size):
    a=b=c=0
    
    for i in s[:size]:
        if i=="a":
            a+=1
        elif i=="b":
            b+=1
        else:
            c+=1
            
    if a>b and a>c:
        return True
    
    for i in range(size,len(s)):
        if s[i]=="a":
            a+=1
        elif s[i]=="b":
            b+=1
        else:
            c+=1
            
        if s[i-size]=="a":
            a-=1
        elif s[i-size]=="b":
            b-=1
        else:
            c-=1
        if a>b and a>c:
            return True
        
    return False
for i in range(int(input())):
    a=input()
    ans=-1
    word=input()
    for i in [2, 3, 4, 7]:
        if i > len(word):
            continue
        if slidingwindow(word,i):
            ans=i
            break
            
    print(ans)
