from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        #ord(c)
        for string in strs:
            lst = [0 for i in range(26)]
            for char in string:
                lst[ord(char) - ord("a")] +=1

            dic[tuple(lst)].append(string)
        
        ret = []
        print(dic)
        for key in dic.keys():
            ret.append(dic[key])
        return ret
        

                
        