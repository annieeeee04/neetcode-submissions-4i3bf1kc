class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        graph = defaultdict(list)

        for s in strs:
            key = str(sorted(s))
            graph[key].append(s)
        
        return list(c for c in graph.values())