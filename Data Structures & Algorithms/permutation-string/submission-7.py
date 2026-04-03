class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # creaete all permuteations of s1 and see if that is a substring of s2
        lens1 = len(s1)
        hashmap = dict()
        def createDic(word, dic):
            for c in word:
                if c not in dic:
                    dic[c] = 0
                dic[c] +=1 
            return
        createDic(s1, hashmap)
        i = 0 
        thisword = dict()
        for i in range(len(s2) -lens1 + 1):
            word = s2[i : i + lens1]
            if i == 0:
                createDic(s2[i:lens1], thisword)
            else:
                # remove last index word and add this index word
                thisword[s2[i -1]] -= 1
                if thisword[s2[i -1]] == 0:
                    del thisword[s2[i -1]]
                if word[-1] not in thisword:
                    thisword[word[-1]] = 0
                thisword[word[-1]] +=1 
            
            # have 2 dictionaries to compare
            if thisword == hashmap:
                return True
            
        return False