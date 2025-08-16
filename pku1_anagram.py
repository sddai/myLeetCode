# 变位词判断
from collections import defaultdict
def anagramSolution(s1:str,s2:str) -> bool:
    s1_dict = defaultdict(int)
    s2_dict = defaultdict(int)
    for i in range(len(s1)):
        s1_dict[s1[i]] += 1
    for i in range(len(s2)):
        s2_dict[s2[i]] += 1
    for i in range(len(s1)):
        flag = (s1_dict[s1[i]] == s2_dict[s2[i]])
        if flag == True:
            continue
        else:
            return False
    return True


print(anagramSolution("cbaebabacd", "abc"))
print(anagramSolution("python", "typonh"))