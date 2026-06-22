class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0]*1001
        for n in trips:
            stops[n[1]]+=n[0]
            stops[n[2]]-=n[0]
        current = 0
        for i in stops:
            current+=i
            if current>capacity:
                return False
        return True

