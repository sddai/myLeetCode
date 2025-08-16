
# 定义一个函数，参数为字符串s和行数numRows，返回值为字符串
def convert( s: str, numRows: int) -> str:

    l = len(s) # length of s
    
    Mat = [[] for _ in range(numRows)]
    
    T = 2*numRows - 2
    
    # 如果行数大于等于字符串长度或者行数为1，直接返回字符串
    if(numRows >= l or numRows==1):
    
        return s
        
    index = 0
    
    # 遍历字符串中的每一个字符
    for i in range(l):
    
        # 如果当前字符的索引除以T的余数小于等于行数减2，则将当前字符添加到当前行的列表中
        if i % (T) <= numRows-2:   # 关于这里为什么是numRows-2而不是-1：因为append之后还要决定index是加一还是减一，最后一行的index是numRows-1，但是到达这一行之后index就要开始减一了，index要从倒数第二行开始都是加一，index是numRows-1时就要执行index-1并进入下一个循环
        
            Mat[index].append(s[i])
            
            index += 1
            
        # 否则，将当前字符添加到上一行的列表中
        else:
        
            Mat[index].append(s[i])
            
            index -= 1
       
    # 返回拼接后的字符串
    return ''.join(s for i in range(numRows) for s in Mat[i])

# 调用函数，参数为字符串PATHY和行数3，打印结果
print(convert("PATHY", 3))