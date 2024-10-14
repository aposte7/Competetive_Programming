class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = len(skill)
        x = skill[0] + skill[l-1]
        chem = skill[0] * skill[l-1]

        for i in range(1,l//2):
            if skill[i] + skill[l-(1+i)] != x:
                return -1
            else:
                chem+= skill[i] * skill[l-(1+i)]
        return chem
        

