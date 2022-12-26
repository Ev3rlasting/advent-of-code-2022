import collections

f = open('input')
lines = f.readlines()
lines = [_.strip() for _ in lines]

MOVES = lines[0]
ORDER = ['-', '+', '⅃', '|', '#']
# x,y offset to left-bottom point of the rectangle box where the shape is in
SHAPE = {
    '-': ((0 + 0j), (1 + 0j), (2 + 0j), (3 + 0j)),
    '+': ((0 + 1j), (1 + 2j), (1 + 1j), (2 + 1j), (1 + 0j)),
    '⅃': ((0 + 0j), (1 + 0j), (2 + 0j), (2 + 1j), (2 + 2j)),
    '|': ((0 + 0j), (0 + 1j), (0 + 2j), (0 + 3j)),
    '#': ((0 + 0j), (0 + 1j), (1 + 1j), (1 + 0j)),
}

DIR = {
    '>': (1 + 0j),
    '<': (-1 + 0j),
}


def getDots(coord, shape):
    return [dotOffset + coord for dotOffset in SHAPE[shape]]


# coord of the left-bottom point of shape box
def canMove(coord, shape):
    for dot in getDots(coord, shape):
        if dot not in DROPPED and 7 > int(dot.real) >= 0 and int(dot.imag) >= 0:
            continue
        else:
            return False
    return True


def fill(coord, shape):
    h = 0
    for dot in getDots(coord, shape):
        DROPPED.add(dot)
        h = max(h, int(dot.imag) + 1)
    return h


def draw(highest, point, shape):
    dots = getDots(point, shape)
    mat = [['.' for _ in range(7)] for _ in range(highest + 4)]
    for dot in dots:
        mat[~int(dot.imag)][int(dot.real)] = '@'
    for dot in DROPPED:
        mat[~int(dot.imag)][int(dot.real)] = '#'
    started = False
    for line in mat:
        if '@' in line: started = True
        if started:
            print(''.join(line))


DROPPED = set()

highest = 0
n = 0
block = 0
diff = ''
prev = 0
N = 2023
while block < N:
    for shape in ORDER:
        block += 1
        diff += str(highest - prev)
        if block == N:
            print('part1', highest)
        prev = highest
        point = complex(2, highest + 3)
        # print(f'Shape "{shape}" starting at {point}, current stack height: {highest}')
        # draw(highest + 3, point, shape)
        while True:
            direction = DIR[MOVES[n % len(MOVES)]]
            nextJetLocation = point + direction
            if canMove(nextJetLocation, shape):
                point = nextJetLocation
            if canMove(point - 1j, shape):
                point = point - 1j
            else:
                highest = max(highest, fill(point, shape))
                n += 1
                # print(f'\tcurrent point at {point}')
                # draw(highest + 3, point, shape)
                break
            n += 1
            # print(f'\tcurrent point at {point}')
            # draw(highest + 3, point, shape)


# COPY paste Robin-Karp algo from online :(
def search(L: int, a: int, MOD: int, n: int, nums) -> str:
    """
    Rabin-Karp with polynomial rolling hash.
    Search a substring of given length
    that occurs at least 2 times.
    @return start position if the substring exits and -1 otherwise.
    """
    # Compute the hash of the substring S[:L].
    h = 0
    for i in range(L):
        h = (h * a + nums[i]) % MOD

    # Store the already seen hash values for substrings of length L.
    seen = collections.defaultdict(list)
    seen[h].append(0)

    # Const value to be used often : a**L % MOD
    aL = pow(a, L, MOD)
    for start in range(1, n - L + 1):
        # Compute the rolling hash in O(1) time
        h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % MOD
        if h in seen:
            # Check if the current substring matches any of the previous substrings with hash h.
            current_substring = nums[start: start + L]
            if any(current_substring == nums[index: index + L] for index in seen[h]):
                return start
        seen[h].append(start)
    return -1


# COPY paste Robin-Karp algo from online :(
def longestDupSubstring(S: str) -> str:
    # Modulus value for the rolling hash function to avoid overflow.
    MOD = 10 ** 13

    # Select a base value for the rolling hash function.
    a = 26
    n = len(S)

    # Convert string to array of integers to implement constant time slice.
    nums = [ord(S[i]) - ord('a') for i in range(n)]

    # Use binary search to find the longest duplicate substring.
    start = -1
    left, right = 1, n - 1
    while left <= right:
        # Guess the length of the longest substring.
        L = left + (right - left) // 2
        start_of_duplicate = search(L, a, MOD, n, nums)

        # If a duplicate substring of length L exists, increase left and store the
        # starting index of the duplicate substring.  Otherwise decrease right.
        if start_of_duplicate != -1:
            left = L + 1
            start = start_of_duplicate
        else:
            right = L - 1

    # The longest substring (if any) begins at index start and ends at start + left.
    return S[start: start + left - 1]


# print(longestDupSubstring(diff))

# the boundary is prefix + repeating part length after worked out from Robin-karp algo
prefix = 290
prefix_l = 184
repeating = [2, 2, 1, 3, 3, 0, 2, 0, 2, 3, 2, 0, 1, 2, 2, 2, 2, 1, 0, 3, 2, 2, 1, 1, 2, 1, 1, 1, 3, 2, 4, 0, 1, 3, 0, 3,
             0, 0, 3, 3, 2, 0, 1, 3, 0, 0, 2, 1, 3, 3, 2, 0, 1, 3, 3, 0, 0, 1, 3, 0, 2, 2, 1, 3, 3, 0, 2, 1, 3, 0, 3, 0,
             0, 3, 3, 2, 0, 1, 3, 0, 3, 2, 1, 3, 3, 2, 0, 1, 1, 3, 2, 0, 1, 2, 1, 3, 0, 1, 3, 3, 2, 2, 1, 3, 2, 1, 1, 1,
             3, 2, 2, 0, 0, 1, 2, 2, 0, 1, 1, 2, 4, 0, 1, 2, 2, 2, 2, 1, 2, 2, 4, 0, 1, 3, 2, 0, 1, 0, 3, 3, 2, 0, 1, 2,
             3, 2, 0, 0, 2, 3, 0, 2, 1, 3, 3, 4, 0, 0, 2, 0, 0, 2, 1, 0, 3, 4, 0, 0, 0, 3, 2, 0, 0, 2, 2, 1, 1, 0, 3, 3,
             2, 0, 1, 3, 3, 0, 0, 0, 2, 2, 2, 2, 0, 0, 1, 2, 0, 0, 3, 2, 4, 0, 1, 3, 3, 0, 2, 1, 3, 3, 2, 0, 1, 2, 2, 2,
             2, 1, 2, 1, 2, 0, 1, 3, 2, 0, 2, 1, 3, 3, 0, 0, 1, 2, 2, 2, 0, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 3, 3, 0, 2,
             1, 3, 3, 2, 2, 1, 2, 1, 4, 2, 1, 2, 3, 0, 2, 1, 3, 3, 4, 0, 0, 2, 2, 4, 2, 0, 2, 2, 2, 0, 1, 3, 3, 2, 2, 1,
             3, 0, 0, 0, 1, 3, 2, 2, 2, 0, 0, 2, 2, 2, 1, 3, 3, 2, 2, 1, 3, 3, 2, 0, 1, 2, 2, 4, 0, 1, 3, 0, 1, 1, 0, 3,
             2, 2, 0, 1, 3, 2, 1, 1, 1, 3, 2, 2, 0, 1, 3, 0, 2, 0, 1, 2, 2, 4, 0, 1, 3, 0, 3, 0, 1, 3, 2, 4, 0, 1, 3, 3,
             4, 0, 1, 3, 2, 2, 2, 1, 3, 3, 0, 0, 1, 3, 3, 4, 0, 0, 0, 3, 2, 0, 0, 1, 3, 2, 0, 1, 3, 2, 4, 0, 1, 3, 3, 2,
             0, 1, 3, 3, 0, 0, 1, 3, 3, 0, 0, 1, 3, 3, 2, 2, 1, 3, 3, 0, 0, 1, 2, 2, 2, 0, 1, 2, 3, 0, 2, 1, 3, 0, 4, 0,
             1, 2, 3, 2, 0, 1, 3, 2, 2, 0, 1, 2, 3, 0, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 1, 1, 3, 2, 0, 0, 0, 2, 1, 2, 0, 1,
             3, 3, 4, 0, 1, 3, 0, 0, 2, 1, 3, 2, 0, 0, 0, 2, 1, 2, 0, 1, 3, 0, 4, 0, 1, 3, 3, 0, 0, 1, 3, 3, 0, 0, 1, 1,
             2, 4, 0, 1, 2, 2, 2, 0, 1, 2, 1, 3, 0, 0, 1, 2, 2, 2, 1, 3, 3, 2, 2, 1, 2, 1, 4, 2, 1, 3, 3, 4, 0, 1, 3, 2,
             2, 2, 1, 2, 3, 2, 0, 1, 3, 3, 0, 2, 1, 2, 2, 1, 0, 0, 3, 2, 4, 2, 1, 2, 3, 2, 0, 1, 2, 1, 4, 0, 0, 1, 2, 4,
             0, 1, 3, 3, 2, 2, 1, 3, 2, 2, 0, 1, 2, 1, 3, 0, 0, 3, 0, 3, 0, 0, 0, 3, 4, 0, 0, 0, 3, 2, 0, 0, 2, 3, 4, 0,
             1, 3, 0, 2, 0, 1, 3, 2, 4, 2, 1, 3, 2, 0, 2, 1, 0, 3, 2, 2, 1, 3, 3, 4, 0, 1, 3, 3, 0, 0, 1, 2, 3, 0, 1, 1,
             3, 0, 2, 2, 1, 3, 2, 2, 0, 1, 3, 3, 0, 0, 1, 2, 3, 0, 0, 0, 3, 3, 2, 2, 1, 3, 3, 0, 0, 1, 3, 3, 4, 0, 0, 2,
             3, 2, 0, 1, 3, 3, 2, 2, 1, 3, 2, 0, 0, 0, 3, 0, 3, 0, 1, 3, 2, 2, 0, 1, 3, 3, 0, 0, 1, 3, 3, 4, 0, 1, 3, 3,
             2, 2, 1, 3, 3, 0, 2, 1, 3, 3, 4, 0, 1, 2, 2, 2, 2, 1, 2, 3, 4, 2, 1, 3, 3, 0, 0, 1, 2, 3, 2, 2, 1, 3, 3, 2,
             0, 1, 3, 0, 4, 2, 1, 3, 2, 2, 0, 1, 3, 3, 4, 0, 1, 3, 3, 2, 2, 1, 3, 2, 4, 0, 1, 3, 2, 2, 0, 1, 3, 0, 3, 0,
             0, 3, 2, 2, 0, 1, 2, 2, 0, 0, 1, 3, 3, 0, 0, 1, 0, 3, 2, 0, 1, 3, 3, 0, 2, 1, 3, 0, 1, 1, 1, 0, 3, 2, 2, 1,
             3, 2, 1, 0, 1, 2, 3, 2, 0, 1, 3, 2, 4, 0, 0, 0, 3, 0, 2, 0, 2, 2, 2, 0, 1, 0, 3, 1, 1, 0, 3, 2, 4, 0, 1, 3,
             3, 2, 0, 1, 2, 2, 1, 1, 1, 3, 2, 0, 0, 1, 2, 3, 0, 0, 1, 2, 2, 0, 2, 1, 3, 2, 0, 0, 1, 2, 3, 2, 2, 1, 3, 3,
             4, 0, 1, 3, 2, 2, 0, 1, 3, 2, 0, 0, 0, 2, 3, 0, 0, 1, 3, 2, 0, 0, 1, 3, 3, 0, 0, 1, 2, 3, 0, 1, 1, 3, 2, 2,
             0, 1, 3, 0, 2, 0, 1, 3, 3, 2, 2, 1, 2, 1, 2, 2, 0, 0, 3, 1, 0, 0, 3, 0, 0, 0, 1, 3, 3, 2, 0, 1, 2, 3, 0, 2,
             0, 3, 0, 2, 0, 1, 3, 3, 2, 0, 1, 3, 3, 4, 2, 0, 3, 2, 0, 0, 1, 3, 2, 4, 0, 1, 3, 0, 3, 0, 1, 3, 0, 0, 0, 1,
             3, 3, 0, 2, 1, 3, 2, 4, 0, 0, 0, 3, 4, 0, 1, 3, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 2, 2, 2, 1, 3, 3, 2, 2, 1, 3,
             2, 0, 2, 1, 3, 2, 4, 2, 1, 2, 2, 0, 2, 1, 3, 3, 0, 2, 1, 2, 2, 2, 0, 0, 2, 1, 3, 2, 1, 1, 2, 2, 0, 1, 3, 0,
             2, 0, 1, 3, 0, 4, 0, 1, 3, 3, 4, 0, 1, 3, 2, 2, 0, 1, 2, 1, 4, 0, 1, 3, 2, 2, 0, 1, 3, 3, 0, 0, 1, 2, 2, 2,
             0, 1, 3, 3, 0, 2, 1, 3, 2, 2, 0, 0, 1, 3, 4, 2, 1, 3, 2, 2, 0, 1, 2, 1, 3, 2, 0, 0, 3, 2, 0, 1, 3, 0, 3, 2,
             1, 2, 2, 2, 2, 0, 0, 3, 2, 2, 1, 3, 3, 2, 0, 1, 2, 3, 0, 2, 1, 3, 3, 4, 0, 0, 3, 3, 2, 0, 1, 1, 2, 4, 0, 1,
             3, 3, 0, 0, 1, 3, 2, 2, 0, 0, 2, 3, 2, 0, 1, 3, 3, 0, 0, 0, 2, 2, 0, 0, 1, 3, 3, 4, 0, 1, 3, 3, 2, 0, 1, 3,
             3, 2, 2, 1, 1, 3, 0, 0, 1, 2, 1, 0, 1, 1, 3, 3, 2, 2, 1, 2, 3, 2, 0, 1, 2, 1, 0, 0, 1, 3, 2, 0, 0, 1, 3, 3,
             2, 2, 1, 1, 2, 1, 0, 0, 3, 3, 0, 2, 1, 3, 3, 4, 0, 1, 2, 1, 3, 2, 1, 3, 3, 2, 0, 1, 2, 1, 2, 0, 1, 2, 3, 2,
             0, 0, 3, 0, 3, 2, 1, 2, 3, 0, 1, 1, 3, 3, 0, 0, 1, 3, 3, 0, 2, 1, 3, 3, 0, 0, 1, 3, 3, 2, 0, 1, 3, 3, 2, 0,
             1, 3, 0, 2, 0, 1, 2, 3, 0, 1, 1, 3, 3, 2, 0, 1, 2, 3, 0, 0, 1, 3, 3, 2, 0, 1, 3, 2, 4, 2, 1, 3, 3, 2, 0, 1,
             3, 2, 0, 0, 1, 3, 2, 2, 2, 1, 3, 2, 1, 1, 1, 3, 2, 4, 2, 1, 3, 3, 2, 0, 1, 2, 1, 2, 0, 0, 3, 3, 0, 0, 0, 2,
             2, 1, 0, 0, 3, 2, 2, 0, 1, 3, 0, 2, 0, 1, 2, 1, 1, 2, 1, 3, 2, 0, 0, 1, 2, 3, 2, 2, 1, 1, 3, 0, 0, 1, 3, 3,
             0, 0, 1, 2, 1, 2, 2, 1, 3, 3, 0, 2, 1, 3, 3, 2, 0, 1, 3, 2, 2, 2, 0, 3, 2, 4, 0, 1, 3, 3, 0, 0, 1, 1, 2, 2,
             2, 1, 3, 0, 4, 2, 1, 2, 2, 2, 2, 1, 3, 2, 2, 2, 1, 2, 3, 0, 0, 0, 2, 1, 2, 0, 1, 3, 3, 2, 0, 1, 3, 3, 4, 0,
             0, 0, 3, 0, 2, 1, 2, 3, 0, 1, 1, 3, 3, 0, 0, 1, 3, 3, 0, 0, 1, 3, 3, 2, 2, 1, 3, 2, 0, 0, 1, 2, 3, 2, 0, 0,
             2, 3, 2, 0, 1, 1, 2, 2, 2, 1, 3, 3, 0, 0, 1, 3, 3, 0, 0, 0, 1, 2, 2, 0, 1, 3, 3, 0, 2, 1, 3, 3, 0, 0, 1, 3,
             2, 0, 1, 1, 2, 1, 2, 0, 1, 3, 3, 0, 2, 1, 3, 0, 3, 0, 0, 2, 2, 2, 2, 1, 3, 2, 2, 0, 0, 3, 3, 0, 2, 0, 3, 0,
             0, 0, 1, 3, 3, 0, 0, 1, 3, 0, 3, 2, 1, 1, 2, 2, 2, 1, 3, 0, 4, 2, 1, 3, 3, 0, 0, 1, 2, 1, 2, 0, 1, 2, 1, 2,
             0, 0, 3, 2, 1, 0, 1, 3, 3, 2, 0, 1, 3, 3, 0, 2, 1, 3, 0, 3, 0, 0, 3, 3, 4, 0, 1, 3, 2, 4, 2, 1, 3, 3, 4, 0,
             1, 3, 2, 2, 2, 1, 3, 2, 1, 1, 1, 2, 1, 0, 0, 1, 2, 1, 3, 0, 1, 3, 2, 0, 0, 1, 3, 2, 0, 2, 0, 0, 3, 1, 2, 0,
             3, 0, 0, 0, 1, 0, 3, 1, 0, 0, 3, 0, 2, 0, 1, 3, 0]
ret = prefix
r, m = divmod(1000000000000 + 1 - prefix_l, len(repeating))
ret += r * sum(repeating) + sum(repeating[:m])
print(ret)
