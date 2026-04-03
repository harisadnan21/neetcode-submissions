class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in range(1,len(digits)+1):
            
            number += digits[-i] * (10 ** (i -1))
        number +=1
        lst = []
    
        while True:
            print(number)
            if number == 0:
                break
            currNum = number %10
            number= number // 10
            lst.append(currNum)

            

        return lst[::-1]
        # idx = len(digits) - 1
        # carry = 0
        # while True:

        #     currNum = digits[idx]
        #     if currNum == 9:
        #         digits[idx] = 0
        #         carry = 1

            

        