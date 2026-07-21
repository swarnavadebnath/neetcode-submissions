class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True
        a,b,c = False,False,False
        for n in triplets:
            if n[0]>target[0] or n[1]>target[1] or n[2]>target[2]:
                continue
            if n[0] == target[0]:
                a = True
            if n[1] == target[1]:
                b = True
            if n[2] == target[2]:
                c = True
            if a and b and c:
                break
        if a and b and c:
            return True
        else:
            return False 
        