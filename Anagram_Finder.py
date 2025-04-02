from collections import Counter

def find_anagrams(filename):

    anagram_groups = {}
    
    with open(filename, 'r') as file:

        for line in file:
            word = line.strip() 

            word_signature = frozenset(Counter(word).items())

            if word_signature not in anagram_groups:
                anagram_groups[word_signature] = []

            anagram_groups[word_signature].append(word)
    
    return list(anagram_groups.values())

def print_anagram_groups(groups):

    for group in groups:
        print(' '.join(group))


filename = "sample.txt"
anagram_groups = find_anagrams(filename)
print_anagram_groups(anagram_groups)
