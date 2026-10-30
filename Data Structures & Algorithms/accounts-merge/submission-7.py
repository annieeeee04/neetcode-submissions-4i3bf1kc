class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_acc = defaultdict(list)
        for i, a in enumerate(accounts):
            for email in a[1:]:
                email_to_acc[email].append(i)
        
        visited = set()
        res = []
        for start in range(len(accounts)):
            if start in visited:
                continue
            
            visited.add(start)
            queue = deque([start])
            emails = set()

            while queue:
                account_idx = queue.popleft()
                for email in accounts[account_idx][1:]:
                    emails.add(email)

                    for nb in email_to_acc[email]:
                        if nb not in visited:
                            visited.add(nb)
                            queue.append(nb)
                    email_to_acc[email].clear()

            res.append([accounts[start][0]] + sorted(emails))
        return res