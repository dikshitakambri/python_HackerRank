# convert a string to a new string where each character in the new string is "(" if that character appears only once 
# in the original string, or ")" if that character appears more than once in the original string.

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

text = input('Input string: ')
answer = duplicate_encode(text)
print(answer)

# "din"      =>  "((("
# "recede"   =>  "()()()"