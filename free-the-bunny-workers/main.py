import enum
import itertools
def solution(num_buns,num_required):
    ans = []


    """
        (       num_buns     )          (       num_buns        )
        (   num_required-1   )      =   (num_buns-num_required+1)       

        Combinations complementary
    
    """
    # Append a list in the list of num_buns
    for i in range(num_buns):
        ans.append([])
    
    numberCopiesOfKey = num_buns-num_required+1
    combinations = list(itertools.combinations(range(num_buns),numberCopiesOfKey))
    lista = enumerate(combinations)
    
    for i,j in lista:
        for k in j:
            ans[k].append(i)
    return ans

print(solution(2,1))
