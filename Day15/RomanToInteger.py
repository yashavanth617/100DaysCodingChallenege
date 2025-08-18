class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1
        }

        prev_value = 0
        total = 0
        for i in s[::-1]:
            value = roman[i]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value
        return total
        
