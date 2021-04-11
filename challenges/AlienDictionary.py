
"""
alien dictionary
"""
class AlienDitionary:
    def isAlienSorted(self, words, order):
        """
        : 953, difficulty = EASY
        : beat 99.12% of submissions
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words)==1:
            return True
        for i in range(0,int(len(words)-1)):
            word1 = str(words[i])
            word2 = str(words[i+1])
            smaller = min(int(len(word1)),int(len(word2)))
            k = 0
            while k<smaller and order.find(str(word1[k]))==order.find(str(word2[k])):
                k+=1
            if k==smaller and smaller == int(len(word2)):
                return False
            if k==smaller and smaller == int(len(word1)):
                break
            if order.find(str(word1[k]))>order.find(str(word2[k])):
                return False
        return True