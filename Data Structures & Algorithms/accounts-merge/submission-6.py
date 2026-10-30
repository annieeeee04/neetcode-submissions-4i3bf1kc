class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parents = list(range(n))

        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        def union(a,b):
            rootA, rootB = find(a), find(b)
            if rootA != rootB:
                parents[rootB] = rootA
        
        emailToAcc = {}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in emailToAcc:
                    union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        groups = defaultdict(list)
        for email, idx in emailToAcc.items():
            groups[find(idx)].append(email)
        
        return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]
