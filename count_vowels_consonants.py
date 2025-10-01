word = input("Enter a word: ")

count = 0
vowel = "aeiou"

for i in word.lower():       
    if i in vowel:
        count = count + 1

print(f"There are {count} vowels in that word.")
