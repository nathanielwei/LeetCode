class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        curr_sum = 0
        while n > 0 and n not in visited and n != 1:
            visited.add(n)
            while n > 0:
                remainder = n%10
                curr_sum += (remainder*remainder)
                n = n//10
            n = curr_sum
            curr_sum = 0

    
        if n == 1:
            return True
        else:
            return False
        

# 1s submission:
# https://leetcode.com/problems/remove-linked-list-elements/?envType=study-plan&id=level-2%3FenvType%3Dstudy-plan&id=level-2
def sum_digit(n: int)-> int:
        str_n = str(n)
        sum_n = 0
        for i in range(len(str_n)):
            sum_n += (int(str_n[i])**2)
        return sum_n

class Solution:
    def isHappy(self, n: int) -> bool:
        e = 0
        while e < 200:
            n = sum_digit(n)
            if n == 1:
                return True
            else:
                e+=1
        return False