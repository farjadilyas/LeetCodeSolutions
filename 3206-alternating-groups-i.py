class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        return sum(((colors[i] != colors[i-1]) and (colors[i-1] == colors[(i+1)%len(colors)]) for i in range(len(colors))))