link : https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ## 시간초과
        # result = 1

        # if x == 0:
        #     return 0
        # elif x == 1:
        #     return 1
        # else:
        #     # if n == 0 :
        #     #     return result

        #     if n < 0 :
        #         for i in range(abs(n)):
        #             result = result * x
                
        #         result = 1 / result

        #     else :
        #         for i in range(n):
        #             result = result * x
        #     return result

        result = 1.0

        if x == 0 or x == 1:
            return 1
        else:
            if n == 0 :
                return result

            if n < 0 :
                result = 1/x * self.myPow(1/x,abs(n)-1)
                return result

            else :
                result = x * self.myPow(x,n-1)
                return result