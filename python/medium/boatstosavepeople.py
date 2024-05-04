class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        start = 0
        end = len(people) - 1
        count = 0

        while(start < end):
            if people[end] == limit:
                end -= 1
                count += 1
            else:
                s = people[start] + people[end]
                if s == limit:
                    start += 1
                    end -= 1
                    count += 1
                elif s > limit:
                    end -= 1
                    count += 1
                else:
                    start += 1
                    end -= 1
                    count += 1
            
            if start == end and people[end] <= limit:
                count += 1
                return count

        return count