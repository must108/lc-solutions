class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        cnt = [1] * n
        res = [0] * n

        def dfs(node, par):
            for child in g[node]:
                if child != par:
                    dfs(child, node)
                    cnt[node] += cnt[child]
                    res[node] += res[child] + cnt[child]

        def dfs1(node, par):
            for child in g[node]:
                if child != par:
                    res[child] = res[node] - cnt[child] + (n - cnt[child])
                    dfs1(child, node)

        dfs(0, -1)
        dfs1(0, -1)

        return res


        