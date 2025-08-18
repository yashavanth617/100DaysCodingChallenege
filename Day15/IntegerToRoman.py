class Solution:
    def intToRoman(self, num: int) -> str:

        values = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        ]

        symbol = [
            'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
        ]
        roman = ""
        i = 0
        while num > 0:
            for _ in range(num // values[i]):
                roman += symbol[i]
                num = num - values[i]
            i += 1
        
        return roman
        
