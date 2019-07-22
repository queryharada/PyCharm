# -*- coding:utf-8 -*-

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz ':
                letters += c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            answer = s[0] == s[-1] and isPal(s[1:-1])
            print(' About to return ', answer, 'For ', s)
            return answer

    return isPal(toChars(s))


if __name__ == "__main__":
    s = 'a[]bc cba@@'
    print(isPalindrome(s))
    s = 'a[]bcba'
    print(isPalindrome(s))
    s = 'dogGod'
    print(isPalindrome(s))
