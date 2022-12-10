class TreeNode:
    def __init__(self, path):
        self.size = None
        self.children_dir = set()
        self.files = set()
        self.parent = None
        self.path = path

    def __hash__(self):
        return hash(str(self.path))

    def __repr__(self):
        return self.path


class FileNode:
    def __init__(self, path, size):
        self.path = path
        self.size = size

    def __hash__(self):
        return hash(str(self.path))

    def __repr__(self):
        return self.path


DIRS = dict()
root = TreeNode('')
DIRS[root.path] = root
currentNode = root
parentNode = root
l = 0
lines = open('input').readlines()
lines = [_.strip() for _ in lines]
while l < len(lines):
    line = lines[l]
    if line.startswith('$ cd '):  # enter a dir
        if line == '$ cd ..':
            currentNode = currentNode.parent
        else:
            if lines[l][5:] != '/':
                node = TreeNode(currentNode.path + lines[l][5:] + '/')
                DIRS[node.path] = node
            else:
                node = TreeNode('/')
            node.parent = currentNode
            currentNode.children_dir.add(node)
            currentNode = node
        print('enterin:', currentNode)
    elif line.startswith('$ ls'):
        print('listing:', currentNode)
        l += 1
        while l < len(lines) and not lines[l].startswith('$'):  # traverse all files/dirs under this dir
            if lines[l].startswith('dir'):  # found new dir
                d = TreeNode(currentNode.path + lines[l][4:] + '/')
                parentNode.children_dir.add(d)
                d.parent = parentNode
                DIRS[d.path] = d
            else:  # single file
                fsize, fname = lines[l].split(' ')
                f = FileNode(currentNode.path + fname, int(fsize))
                currentNode.files.add(f)
                print(f'adding file: {f} to {currentNode}')
            l += 1
        l -= 1
    l += 1

del DIRS['']


def get_total(node: TreeNode):
    fsize_all = sum([ff.size for ff in node.files])
    if node.children_dir:
        fsize_all += sum(get_total(dd) for dd in node.children_dir)
    node.size = fsize_all
    return fsize_all


occupied = 70000000 - get_total(root)
ret = float('inf')
for d in DIRS.values():
    if occupied + d.size >= 30000000:
        ret = min(ret, d.size)
print(ret)
