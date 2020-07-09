# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

letter_count = {}
final_hash = {}
final_text = ""

with open("applications/crack_caesar/ciphertext.txt", encoding="utf-8") as cipher_text:
    cipher = cipher_text.read()
top_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
for letter in cipher:
    if letter.isalpha():
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
sort_list = list(letter_count.items())
sort_list.sort(reverse=True, key = lambda item: item[1])
print(sort_list)
for i, element in enumerate(top_letters):
    final_hash[sort_list[i][0]] = top_letters[i]

for letter in cipher:
    if letter.isalpha():
        final_text += final_hash[letter]
    else:
        final_text += letter
print(final_text)