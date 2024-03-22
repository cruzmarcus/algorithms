# 1 Valid anagram
from collections import Counter

def are_anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


def are_anagrams_counter(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)


are_anagrams_counter('asb', "abc") 