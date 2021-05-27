from typing import List


class Solution(object):
    def shortestDistance(self, wordsList: List[str], word1: str, word2: str) -> int:
        w1_pos = 0
        w2_pos = 0
        min_dist = 99999999
        for w in range(len(wordsList)):
            if word1 == wordsList[w]:
                w1_pos = w + 1
                if w2_pos > 0 and abs(w2_pos - w1_pos) < min_dist:
                    min_dist = abs(w2_pos - w1_pos)
            elif word2 == wordsList[w]:
                w2_pos = w + 1
                if w1_pos > 0 and abs(w2_pos - w1_pos) < min_dist:
                    min_dist = abs(w2_pos - w1_pos)
            if min_dist == 1:
                return min_dist
        return min_dist


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestDistance(["perfect", "makes", "practice", "coding", "makes"], "practice", "coding"))
    print(sol.shortestDistance(["perfect", "makes", "practice", "coding", "makes"], "makes", "coding"))
    print(sol.shortestDistance(["perfect", "coding", "practice", "makes", "makes"], "perfect", "makes"))