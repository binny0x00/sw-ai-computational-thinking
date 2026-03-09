# link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

        result = []
        # "23"
        def backtrack(start, current_str):
            print(start, current_str)
            # if 해를 찾으면 저장
            if len(current_str) == len(digits):
                result.append(current_str)
                return

            # for 선택지 in 후보들
            for letter in letters[int(digits[start])-2]:
                # if 유망한가
                # 선택
                # 탐색
                backtrack(start+1,current_str + letter)
                # 취소
                # 문자열은 불변이라 생략

        backtrack(0,"")
        return result