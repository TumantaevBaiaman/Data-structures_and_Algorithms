"""
Сгруппировать  слова  по общим буквам

Sample Input:
["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output:
[["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
"""


def grouping(words: list) -> list:

    def keybyword(word: str) -> str:
        symcnt = {}
        for sym in word:
            if sym not in symcnt:
                symcnt[sym] = 0
            symcnt[sym] += 1
        lst = []
        for sym in sorted(symcnt.keys()):
            lst.append(sym)
            lst.append(str(symcnt[sym]))
        return ''.join(lst)

    groups = {}
    for word in words:
        sortedword = keybyword(word)
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans