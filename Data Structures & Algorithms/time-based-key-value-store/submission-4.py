class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic.keys():
            self.dic[key] = []
        self.dic[key].append([timestamp, value])
        return None

        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        lst = self.dic[key]
        lenlst = len(lst)
        l= 0
        r = lenlst -1
        while l <= r:
            m = (l +r) // 2

            if (m == lenlst -1 and lst[m][0] <= timestamp) or (m != lenlst -1 and lst[m + 1][0] > timestamp and lst[m][0] <= timestamp):
                return lst[m][1]
            elif lst[m][0] > timestamp:
                r = m -1
            else:
                l = m + 1

        return ""
