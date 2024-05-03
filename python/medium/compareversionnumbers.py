class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = list(map(int, version1.split('.')))
        arr2 = list(map(int, version2.split('.')))

        n = len(arr1)
        m = len(arr2)

        if n < m:
            while m != n:
                arr1.append(0)
                n += 1
        elif n > m:
            while n != m:
                arr2.append(0)
                m += 1

        if arr1 < arr2:
            return -1
        elif arr1 > arr2:
            return 1
        else:
            return 0
