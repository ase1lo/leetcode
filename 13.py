class Solution:
    def romanToInt(self, s: str) -> int:
        decode = 0
        n = 0
        if s[0:2] == 'IX' and len(s) == 2:
            decode += 9
        elif s[0:2] == 'IX' and len(s) != 2:
            print(decode)  
            return False
        elif s[0:2] == 'IV' and len(s) == 2:
            decode += 4
        elif s[0:2] == 'IV' and len(s) != 2:
            print(decode)  
            return False
        else:
            pred_num = 1001
            for i in range(len(s)):
                match s[i]:
                    case 'I':
                        n = 1
                    case 'V':
                        n = 5
                    case 'X':
                        n = 10
                    case 'L':
                        n = 50
                    case 'C':
                        n = 100
                    case 'D':
                        n = 500
                    case 'M':
                        n = 1000
                if n > pred_num:
                    print(decode)  
                    return False
                else:
                    decode += n
                    pred_num = n     
        return decode
    


solve = Solution()

print(solve.romanToInt('MCMXCIV'))