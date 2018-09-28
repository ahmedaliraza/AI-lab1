vowel = ['a', 'e', 'i', 'o', 'u']
str = input("Enter a string: ")
count = 0
for letter in str:
    if letter in vowel:
        count += 1
print(count)