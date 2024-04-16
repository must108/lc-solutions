class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = []
        count = 0

        for i in students:
            q.append(i)

        i = 0
        while len(q) > 0 and count is not len(q):
            if q[0] == sandwiches[i]:
                count = 0
                q.pop(0)
                i += 1
            else:
                x = q[0]
                q.pop(0)
                q.append(x)
                count += 1

        return len(q)