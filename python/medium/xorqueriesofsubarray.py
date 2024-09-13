class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ret = []

        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]

        for i, j in queries:
            if i > 0:
                ret.append(arr[i-1] ^ arr[j])
            else:
                ret.append(arr[j])

        return ret