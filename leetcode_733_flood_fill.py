from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    old = image[sr][sc]
    image[sr][sc] = newColor

    if 0 <= sr - 1 < len(image) and image[sr - 1][sc] == old and image[sr - 1][sc] != newColor:
        floodFill(image, sr - 1, sc, newColor)
    if 0 <= sr + 1 < len(image) and image[sr + 1][sc] == old and image[sr + 1][sc] != newColor:
        floodFill(image, sr + 1, sc, newColor)
    if 0 <= sc - 1 < len(image[0]) and image[sr][sc - 1] == old and image[sr][sc - 1] != newColor:
        floodFill(image, sr, sc - 1, newColor)
    if 0 <= sc + 1 < len(image[0]) and image[sr][sc + 1] == old and image[sr][sc + 1] != newColor:
        floodFill(image, sr, sc + 1, newColor)


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2

floodFill(image, sr, sc, newColor)

print(image)
