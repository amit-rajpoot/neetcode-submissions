class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = 1

        if x < 0:
            sign = -1
            x = abs(x)

        while x > 0:
            rem = x % 10
            result = (result * 10) + rem
            x = x // 10
        
        result = sign * result
        if not -2147483648 <= result <= 2147483647:
            return 0
        
        return result