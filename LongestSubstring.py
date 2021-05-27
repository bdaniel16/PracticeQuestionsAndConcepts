def lengthOfLongestSubstring(s: str) -> int:
    """
    "abcabcbb"
    mp = {} l = 0 r = 0 m = 0
    m =1 mp = {'a': 1} l=0,r=0
    m =2 mp = {'a' : 1, 'b': 2} l=0 r=1
    m =3 mp = {'a' : 1, 'b': 2, 'c':3} l =0, r=2
    l = 1, r=3, m=3 mp = {'a' : 4, 'b': 2, 'c':3}
    l=2, r=4, m=3 mp = {'a' : 4, 'b': 5, 'c':3}
    l = 3, r=5, m=3 mp = {'a' : 4, 'b': 5, 'c':6}
    l=5, r=6, m=3 mp = {'a' : 4, 'b': 7, 'c':6}
    l=7, r=7 m=3 mp = {'a' : 4, 'b': 8, 'c':6}
    -----------
    "bbbb"
    "pwwkew"

    """
    str_map = {}
    sub_max = 0
    left = 0
    for right in range(len(s)):
        if str_map.get(s[right]):
            left = max(str_map[s[right]], left)
        sub_max = max(sub_max, right - left + 1)
        str_map[s[right]] = right + 1
    return sub_max


if __name__ == "__main__":
    print(lengthOfLongestSubstring(" "))