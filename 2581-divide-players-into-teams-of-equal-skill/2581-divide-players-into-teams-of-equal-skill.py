class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l = 0
        r = len(skill)-1
        skill.sort()
        sum = skill[l] + skill[r]
        chem = skill[l] * skill[r]
        l+=1
        r-=1
        while l < r:
            if skill[l] + skill[r] != sum:
                return -1
            chem+=  skill[l] * skill[r]
            l+=1
            r-=1
        return chem



