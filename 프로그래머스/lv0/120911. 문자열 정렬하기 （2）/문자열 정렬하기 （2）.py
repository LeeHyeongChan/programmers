def solution(my_string):
    string = my_string.lower()
    answer = ''.join(sorted(string))

    return answer