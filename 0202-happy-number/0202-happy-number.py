class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfEachSquare(n)
            if n == 1:
                return True
        return False


    def sumOfEachSquare(self, num: int) -> int:
        curr_sum = 0
        while num != 0:
            curr_sum += (num % 10)**2
            num //= 10
        return curr_sum
        