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
                parent[rootB] = rootA
        
        emailToAcc = defaultdict(list)
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in emailToAcc:
                    union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        groups = defaultdict(list)
        for email, i in emailToAcc.items():
            groups[find(i)].append(email)
        
        return [[accounts[root][0]] + emails for root, emails in groups.items()]