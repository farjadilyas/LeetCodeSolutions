unit_arr = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
one_tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"]
tens_arr = [None, None, "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


class Solution:
    def numberToWords(self, num: int) -> str:
        if not num: return "Zero"

        def unit_tens(num):
            if not num:
                return ""
            tens, unit = divmod(num, 10)
            if not tens:
                return unit_arr[unit]
            if tens == 1:
                return one_tens[unit]
            return tens_arr[tens] if not unit else f"{tens_arr[tens]} {unit_arr[unit]}"

        digits = []
        remainder = num
        for i in range(12):
            remainder, digit = divmod(remainder, 10)
            digits.append(digit)
        digits = digits[::-1]
        ans = []

        def process_threes(starting_idx, group_name):
            if digits[starting_idx]:
                ans.append(f"{unit_arr[digits[starting_idx]]} Hundred")
            if digits[starting_idx + 1] or digits[starting_idx + 2]:
                ans.append(unit_tens((digits[starting_idx + 1] * 10) + digits[starting_idx + 2]))
            if (digits[starting_idx] or digits[starting_idx + 1] or digits[starting_idx + 2]) and group_name:
                ans.append(group_name)

        process_threes(0, "Billion")
        process_threes(3, "Million")
        process_threes(6, "Thousand")
        process_threes(9, None)
        return ' '.join(ans)
