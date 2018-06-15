class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0:
            return ''
        res = 0
        stop = False
        m = len(strs[0])
        for str1 in strs:
            m = min(m, len(str1))
        for i in range(m):
            c = strs[0][i]
            for j in range(1, n):
                if c != strs[j][i]:
                    res -= 1
                    stop = True
                    break
            res += 1
            if stop:
                break
        return strs[0][:res]

print(Solution().longestCommonPrefix(["aca","cba"]))