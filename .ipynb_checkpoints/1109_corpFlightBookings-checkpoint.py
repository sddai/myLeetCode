class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats
        answer = [0] * n
        for i in range(n):
            if i == 0:
                answer[i] = diff[0]
            else:
                answer[i] = answer[i - 1] + diff[i]
        return answer 
