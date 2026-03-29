class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        graph = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            graph[key].append(s)

        return list(graph.values())