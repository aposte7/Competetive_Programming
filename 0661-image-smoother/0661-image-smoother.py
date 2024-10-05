class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(img), len(img[0])

        res = [[0]*COL for _ in range(ROW)]
        for i in range(ROW):
            for j in range(COL):
                t ,n =0,0
                for x in range(i-1,i+2):
                    for y in range(j-1, j+2):
                        if x < 0 or x == ROW or y < 0 or y == COL:
                            continue;
                        t += img[x][y]
                        n += 1
                res[i][j]=t // n
        return res
                        
                    

        