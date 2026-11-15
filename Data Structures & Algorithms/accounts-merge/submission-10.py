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
                parent[rootA] = rootB

        emailToAcc = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        group = defaultdict(list)
        for email, i in emailToAcc.items():
            group[find(i)].append(email)
        
        return [[accounts[root][0]] + emails for root, emails in group.items()]