def validate_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

print(validate_anagrams("python", "c#"))
print(validate_anagrams("man", "woman"))
print(validate_anagrams("Tiger", "Lion"))
print(validate_anagrams("Cinema", "Iceman"))
