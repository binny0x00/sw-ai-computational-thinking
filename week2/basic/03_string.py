"""
[문자열 - 회문(Palindrome) 판별]

문제 설명:
- 주어진 문자열이 회문(앞에서 읽으나 뒤에서 읽으나 같은 문자열)인지 판별합니다.
- 대소문자를 구분하지 않고, 공백과 특수문자는 무시합니다.

입력:
- s: 판별할 문자열

출력:
- True: 회문인 경우
- False: 회문이 아닌 경우

예제:
입력: "A man, a plan, a canal: Panama"
출력: True

입력: "race a car"
출력: False

힌트:
- 알파벳과 숫자만 남기고 소문자로 변환하세요
- 문자열을 뒤집어서 비교하거나, 양 끝에서 시작해 중앙으로 이동하며 비교하세요
"""

def is_palindrome(s):
    """
    문자열이 회문인지 판별하는 함수
    
    Args:
        s: 판별할 문자열
    
    Returns:
        bool: 회문이면 True, 아니면 False
    """
    # TODO: 알파벳과 숫자만 남기고 소문자로 변환하세요
    # 힌트: isalnum() 메서드와 lower() 메서드 사용

    # isalpha() : 문자열이 영어 or 한글로 되어 있으면 true 리턴
    # isalnum() : 문자열이 영어 or 한글 or 숫자로 되어 있으면 true 리턴

    # 문자열 정제
    # 1) 문자열에서 영어, 한글, 숫자만 필터링 - .isalnum() 사용
    # 2) 영어 알파벳 소문자 통일 - .lower() 사용

    # s = "".join([x for x in s.lower() if x.isalnum()])
    # 대신에 제너레이터를 사용해 하나씩 만들어서 join하는 방법 있음
    # 제너레이터 : 한 번에 하나씩 구성요성를 반환해주는 이터러블을 생성해주는 객체
    # 이터러블 : 순회할 수 있는 객체
    # s = "".join(x.lower() for x in s if x.isalnum())
    
    # TODO: 정제된 문자열이 회문인지 확인하세요
    # 방법1: 문자열을 뒤집어서 비교 ([::-1] 사용)
    # 방법2: 양 끝 인덱스를 이용한 투 포인터 방식

    # 필수 조건
    # 모두 소문자로 만들것
    # 알파벳, 숫자만 비교할 것
    # 회문인지 여부를 반환할 것

    # 문자열 정제 후 뒤집기 비교
    # 문자열 정제 후 투포인터
    # 정제 없이 투포인터
      
    # # 방법 2(1) 문자열 정제 후 투포인터 - 시간 복잡도 : O(n), 공간 복잡도 : O(n) - 파이썬 문자열은 불변
    # s = "".join(x.lower() for x in s if x.isalnum())

    # for x in range(len(s)//2):
    #   if s[x] != s[len(s)-1-x]:
    #     return False
      
    # return True

    # 방법 2(2) 문자열 정제 없이 투포인터 - 시간 복잡도 : O(n), 공간 복잡도 : O(1)
    """
    투 포인터

    left = 0
    right = len(s) - 1

    반복 조건 : while left < right:

    비교할 값이 알파벳/숫자가 아니라면 한칸 이동
    비교할 값이 알파벳/숫자라면 lower()로 비교

    끝까지 통과하면 True

    """

    left = 0
    right = len(s)-1

    while left < right:
        if not (s[left].isalnum()):
            left += 1
            continue
        if not (s[right].isalnum()):
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left +=1
        right -=1
    return True

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")


