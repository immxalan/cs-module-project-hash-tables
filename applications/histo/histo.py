# Your code here

f = open("applications/histo/robin.txt", "r")
remove_chars = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\",
               "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", '', "!", "?"]
space = " "

cache = {}
word = ""

for x in f.read().lower():
    if x in remove_chars:
        continue

    if x == space or x == "\n":
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
        word = ""
    else:
        word += x


print(cache)

a = sorted(cache.items(), key=lambda keyAndVal: (keyAndVal[1], keyAndVal[0]))

a = a[::-1]
# print(a)
str = ""
number_of_spaces = 20

for item in a:
    str += item[0]

    for i in range(0, number_of_spaces - len(str)):
        str += " "

    for i in range(0, item[1]):
        str += "*"
    print(str)
    str = ""