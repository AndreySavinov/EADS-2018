def split(arr, level):
    if len(arr) > 1:
        arr = list(sorted(arr, key=lambda p: p[level]))
    med = arr[len(arr)//2]
    left, right = arr[:len(arr)//2], arr[len(arr)//2+1:]
    return med, left, right


def is_inside_corners(point, corners):
    minimums, maximums = corners
    return all(left <= p < right for left, p, right in zip(minimums, point, maximums))


class KDTree(object):
    def __init__(self, points, base, level=0):
        self.level = level
        self.level = level
        self.base = base
        self.med, left, right = split(points, level)
        if left:
            self.left = KDTree(left, base, (level + 1) % base)
        else:
            self.left = None
        if right:
            self.right = KDTree(right, base, (level + 1) % base)
        else:
            self.right = None

    def query_corners(self, corners, result=None):
        minimums, maximums = corners
        if result is None:
            result = []
        if is_inside_corners(self.med, corners):
            result.append(self.med)
        if self.right is not None and self.med[self.level] < maximums[self.level]:
            self.right.query_corners(corners, result)
        if self.left is not None and minimums[self.level] <= self.med[self.level]:
            self.left.query_corners(corners, result)
        return result

    def query_corners_multi(self, *many_corners):
        result = set()
        for corners in many_corners:
            result.update(self.query_corners(corners))
        return list(result)

    def as_dict(self, root=None):
        if root is None:
            root = dict()
        root['level'] = self.level
        root['med'] = self.med
        if self.left is not None:
            root['left'] = left = dict()
            self.left.as_dict(left)
        else:
            root['left'] = None
        if self.right is not None:
            root['right'] = right = dict()
            self.right.as_dict(right)
        else:
            root['right'] = None
        return root

    

if __name__ == '__main__':
    with open('input.txt') as inp:
        num_mines = int(inp.readline())
        mines = []
        for _ in range(num_mines):
            x, y, p = map(int, inp.readline().split())
            mines.append((x, y, p))
        coal_mine = KDTree(points=mines, base=2)

        num_queries = int(inp.readline())
        query_results = []
        for _ in range(num_queries):
            num_rectangles = int(inp.readline())
            rectangles = []
            for _ in range(num_rectangles):
                x1, y2, x2, y1 = map(int, inp.readline().split())
                rectangles.append(((x1, y1), (x2, y2)))
            points = coal_mine.query_corners_multi(*rectangles)
            query_results.append(sum(p[2] for p in points))
    with open('output.txt', 'w') as out:
        out.write('\n'.join(map(str, query_results)))
