class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        directions = {"r": "d", "d": "l", "l": "u", "u": "r"}

        limits = {
            "u": 0,
            "d": len(matrix) - 1,
            "r": len(matrix[0]) - 1,
            "l": 0
        }

        d = "r"
        currIdx = [0, 0]
        total = len(matrix) * len(matrix[0])

        while len(ret) != total:
            ret.append(matrix[currIdx[0]][currIdx[1]])

            if d == "r":
                if currIdx[1] + 1 <= limits["r"]:
                    currIdx = [currIdx[0], currIdx[1] + 1]
                else:
                    limits["u"] += 1              # FIX: shrink top
                    d = directions[d]
                    if len(ret) != total:
                        currIdx = [currIdx[0] + 1, currIdx[1]]  # step into next dir

            elif d == "d":
                if currIdx[0] + 1 <= limits["d"]:
                    currIdx = [currIdx[0] + 1, currIdx[1]]
                else:
                    limits["r"] -= 1              # FIX: shrink right
                    d = directions[d]
                    if len(ret) != total:
                        currIdx = [currIdx[0], currIdx[1] - 1]

            elif d == "l":
                if currIdx[1] - 1 >= limits["l"]:
                    currIdx = [currIdx[0], currIdx[1] - 1]
                else:
                    limits["d"] -= 1              # FIX: shrink bottom
                    d = directions[d]
                    if len(ret) != total:
                        currIdx = [currIdx[0] - 1, currIdx[1]]

            else:  # d == "u"
                if currIdx[0] - 1 >= limits["u"]:
                    currIdx = [currIdx[0] - 1, currIdx[1]]
                else:
                    limits["l"] += 1              # FIX: shrink left
                    d = directions[d]
                    if len(ret) != total:
                        currIdx = [currIdx[0], currIdx[1] + 1]

        return ret