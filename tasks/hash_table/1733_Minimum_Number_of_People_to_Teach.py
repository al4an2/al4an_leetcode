import collections
class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        
        f_with_p = set()
        lang_freq = collections.defaultdict(int)
        languages_s = [set(x) for x in languages]

        for friendship in friendships:
            f1 = friendship[0] - 1
            f2 = friendship[1] - 1

            if languages_s[f1] > languages_s[f2]:
                f1, f2 = f2, f1
            if not languages_s[f1] & languages_s[f2]:
                f_with_p.add(f1)
                f_with_p.add(f2)


        for p in f_with_p:
            for l in languages[p]:
                lang_freq[l] += 1

        
        return len(f_with_p) - max(lang_freq.values()) if lang_freq else 0

# O(E·k + M·k)