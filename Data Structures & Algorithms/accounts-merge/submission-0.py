class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a,b):
            rootA, rootB = find(a), find(b)
            if rootA != rootB:
                parent[rootB] = rootA
        
        emailToAccount = {}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in emailToAccount:
                    union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i
        
        group = defaultdict(list)
        for email, idx in emailToAccount.items():
            group[find(idx)].append(email)

        return [[accounts[root][0]] + sorted(emails) for root, emails in group.items()]