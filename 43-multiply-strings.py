from itertools import zip_longest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        if num2[0] == '0':
            return '0'
        max_len = len(num1) + 1
        results = []
        for n2idx, n2 in enumerate(reversed(num2)):
            res = [0 for _ in range(n2idx)]
            carry = 0
            for n1 in reversed(num1):
                tmp = (int(n2) * int(n1)) + carry
                carry, tmp = divmod(tmp, 10)
                res.append(tmp)
            if carry:
                res.append(carry)
            results.append(res)
        result = []
        carry = 0
        for vals in itertools.zip_longest(*results, fillvalue=0):
            carry, rs = divmod(sum(vals) + carry, 10)
            result.append(rs)
        if carry:
            result.append(carry)
        return ''.join(str(e) for e in reversed(result))
