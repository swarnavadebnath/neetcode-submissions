class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for b in bills:
            if b == 5:
                five+=1
            if b == 10:
                ten+=1
                if five:
                    five-=1
                else:
                    return False
            if b == 20:
                if five and ten:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
        