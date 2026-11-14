class Solution(object):
    def isAnagram(self, s, t):
        x = list(t)
        y = list(s)
        if len(s) == len(t):
            for i in x:
                if i not in y:
                    return False
                if i in y:
                    y.remove(i)
            return True        
        else:
            return False