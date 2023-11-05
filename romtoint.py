class Solution(object):
    def romanToInt(self, s):
        romanToInteger = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev_value = 0

        for c in s[::-1]:
            value = romanToInteger[c]

            if value < prev_value:
                result -= value
            else:
                result += value

            prev_value = value

        return result


solution = Solution()
roman_numeral = "MCMXCIV"
int_value = solution.romanToInt(roman_numeral)
print(int_value)
