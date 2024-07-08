class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ind ={c:i for i,c in enumerate(order)}
        sort_v=sorted(words,key=lambda x: [ind[y] for y in x])
        return words == sort_v