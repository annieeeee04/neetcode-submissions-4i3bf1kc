# Time: O(K * α(N) + K log K), N = number of accounts, K = total number of emails
# Space: O(N + K)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))

        # Time: O(α(N)) with path compression
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        # Time: O(K * α(N))
        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA != rootB:
                parent[rootB] = rootA
        
        emailToAcc = {}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in emailToAcc:
                    union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        groups = defaultdict(list)
        for email, acc in emailToAcc.items():
            groups[find(acc)].append(email)
        
        return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]