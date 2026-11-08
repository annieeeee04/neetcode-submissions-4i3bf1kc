class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n)) 
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(u,v):
            rootA, rootB = find(u), find(v)
            if rootA != rootB:
                parent[rootA] = rootB
        
        emailToAcc = defaultdict(list)
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in emailToAcc:
                    emailToAcc[email] = i
                else:
                    union(emailToAcc[email], i)
        
        groups = defaultdict(list)
        for email, acc in emailToAcc.items():
            groups[find(acc)].append(email)
        
        return [[accounts[root][0]] + emails for root, emails in groups.items()]
