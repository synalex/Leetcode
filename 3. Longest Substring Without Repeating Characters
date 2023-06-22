class Solution:
    '''
    Problem: Longest Substring Without Repeating Characters
    input: string: s
    output: int: length of substring
    constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.  
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        record = 1 
        substring = []
        for char in s:
            if substring:
                if char not in substring:
                    substring.append(char)
                else:
                    record = max(len(substring), record)
                    for i in range(len(substring)-1, -1, -1):
                        if char == substring[i]:
                            substring = substring[i+1:]
                            break
                        else:
                            pass
                    substring.append(char)
            else:
                substring.append(char)

        return max(record, len(substring))
