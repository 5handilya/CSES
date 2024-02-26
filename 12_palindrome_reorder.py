def gen_palindrome(freq):
    palindrome = []
    odd_char = None
    total_chars = sum(freq.values())
    for char, count in freq.items():
        palindrome.extend([char] * (count // 2))
        if count % 2 != 0:
            odd_char = char
    palindrome += palindrome[::-1]
    if odd_char is not None:
        palindrome.insert(total_chars // 2, odd_char)
    return ''.join(palindrome)

def count_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def check_palindrome_possible(s):
    freq = count_frequency(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    if (len(s) % 2 == 0 and odd_count > 0) or (len(s) % 2 != 0 and odd_count != 1):
        print("NO SOLUTION")
    else:
        print(gen_palindrome(freq))

n = input()
check_palindrome_possible(n)
