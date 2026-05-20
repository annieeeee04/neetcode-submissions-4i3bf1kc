class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        for c in strs:
            key = str(sorted(c))
            graph[key].append(c)
        return list(s for s in graph.values())