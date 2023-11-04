class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        lr, lc = len(image), len(image[0])
        target = image[sr][sc]
        def recurse(r, c):
            if image[r][c] != target:
                return
            image[r][c] = color
            if r-1 >= 0:
                recurse(r-1, c)
            if c+1 < lc:
                recurse(r, c+1)
            if r+1 < lr:
                recurse(r+1, c)
            if c-1 >= 0:
                recurse(r, c-1)
        if target != color:
            recurse(sr, sc)
        return image
