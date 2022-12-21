def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    def make_number(str1, str2):
        if str1 != "" and is_prime(int(str1)):
            made_num.add(int(str1))
        
        for i in range(len(str2)):
            make_number(str1 + str2[i], str2[:i] + str2[i+1:])

    made_num = set()
    make_number("", numbers)

    answer = len(made_num)
    return answer



print(solution("17"))