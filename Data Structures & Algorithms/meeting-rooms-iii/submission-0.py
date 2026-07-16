class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [0] * n
        count = [0] * n
        for s,e in meetings:
            minroom = 0
            found = False
            for i in range(n):
                if rooms[i] <= s:
                    found = True
                    count[i]+=1
                    rooms[i] = e
                    break
                if rooms[minroom]>rooms[i]:
                    minroom = i
            if found:
                continue
            count[minroom] += 1
            rooms[minroom] += e - s
        return count.index(max(count))

        