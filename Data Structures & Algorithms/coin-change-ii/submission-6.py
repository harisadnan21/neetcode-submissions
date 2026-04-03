class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ret = 0 
        dic = {}
        def recurse(curr_amount, curr_idx):
            print(curr_amount)
            if curr_amount> amount or curr_idx > len(coins) -1:
                return 0
            if curr_amount == amount:
                return 1
            first = second = 0
            if (curr_amount + coins[curr_idx], curr_idx) in dic:
                first = dic[(curr_amount + coins[curr_idx], curr_idx)]
            else:
                first = dic[(curr_amount + coins[curr_idx], curr_idx)] = recurse(curr_amount + coins[curr_idx], curr_idx)
            
            if (curr_amount, curr_idx + 1) in dic:
                second = dic[(curr_amount, curr_idx + 1)]
            else:
                second = dic[(curr_amount, curr_idx + 1)] = recurse(curr_amount, curr_idx + 1)

            return first + second
        
        return recurse(0, 0)
