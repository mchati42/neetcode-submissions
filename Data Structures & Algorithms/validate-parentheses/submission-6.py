class Solution:
    def isValid(self, s: str) -> bool:
        self.s = s
        lis = list(s)
        i = 0
        while(i < len(lis) - 1):
            print(f"lis[i] ----{lis[i]}")
            if lis[i] == '(' and lis[i + 1] == ')':
                lis.remove(lis[i])
                lis.remove(lis[i])
                i = 0
            elif lis[i] == '[' and lis[i + 1] == ']':
                lis.remove(lis[i])
                lis.remove(lis[i])
                i = 0
            elif lis[i] == '{' and lis[i + 1] == '}':
                lis.remove(lis[i])
                lis.remove(lis[i])
                i = 0
            else:
                i += 1
        return len(lis) == 0