
def convert( s: str, numRows: int) -> str:

    l = len(s) # length of s
    
    Mat = [[] for _ in range(numRows)]
    
    T = 2*numRows - 2
    
    if(numRows >= l or numRows==1):
    
        return s
        
    index = 0
    
    for i in range(l):
    
        if i % (T) <= numRows-2:   # 关于这里为什么是numRows-2而不是-1：因为append之后还要决定index是加一还是减一，最后一行的index是numRows-1，但是到达这一行之后index就要开始减一了，index要从倒数第二行开始都是加一，index是numRows-1时就要执行index-1并进入下一个循环
        
            Mat[index].append(s[i])
            
            index += 1
            
        else:
        
            Mat[index].append(s[i])
            
            index -= 1
       
    return ''.join(s for i in range(numRows) for s in Mat[i])

print(convert("PATHY", 3))
