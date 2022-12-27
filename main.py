from math import sqrt


def countBitsRough(n):
    l = [0,1,1,2,1,2,2,3]
    if n < 8:
        return l[:n+1]

    c_n = n
    next_power_stage = 1
    next_power = 0
    cur_power = 3
    cur_len = 8
    while c_n > 1:
        c_n /= 2
        next_power += 1
        next_power_stage *= 2
    print(next_power_stage, next_power)

    for cur_power in range(3, next_power):
        print(f"Calculating for power {cur_power}, range: {2**cur_power} - {2**(cur_power+1)-1}")
        num_iter = cur_len if cur_len*2 <= n else n + 1 - cur_len
        print(f"BC: cur_len {cur_len*2}, n: {n}, num_iter: {num_iter}")
        for i in range(num_iter):
            #print(f"Calculating for {cur_len+i}: {l[i]+1}")
            l.append(l[i]+1)
        cur_len *= 2

    if n == next_power_stage:
        l.append(1)
    return l


def countBits(n):
    l = [0,1,1,2]
    if n < 4:
        return l[:n+1]

    c_n = n
    next_power_stage = 1
    next_power = 0
    cur_len = 4
    while c_n > 1:
        c_n /= 2
        next_power += 1
        next_power_stage *= 2
    print(next_power_stage, next_power)

    for cur_power in range(2, next_power):
        print(f"Calculating for power {cur_power}, range: {2**cur_power} - {2**(cur_power+1)-1}")
        num_iter = cur_len if cur_len*2 <= n else n + 1 - cur_len
        print(f"BC: cur_len {cur_len*2}, n: {n}, num_iter: {num_iter}")
        for i in range(num_iter):
            print(f"Calculating for {cur_len+i}: {l[i]+1}")
            l.append(l[i]+1)
        cur_len *= 2

    if n == next_power_stage:
        l.append(1)
    return l


def maxSubArray(nums):
    cur_start_idx = None
    max_elem = -(10**4)+1
    running_total = 0
    true_max_running_total = 0

    for idx, elem in enumerate(nums):
        max_elem = max(elem, max_elem)
        print(f"elem: {elem} {running_total}")
        if cur_start_idx is None and elem >= 0:
            print(f"starting new at: {idx}")
            cur_start_idx = idx
            running_total = elem
        elif running_total + elem > 0:
            running_total += elem
        else:
            running_total = 0
            cur_start_idx = None

        print(f"end: {idx} {running_total} {true_max_running_total}")
        true_max_running_total = max(running_total, true_max_running_total)

    return max_elem if true_max_running_total == 0 else true_max_running_total


def maxSumAfterPartitioningRough(arr, k):
    arr_len = len(arr)
    dp = [0 for _ in range(arr_len)]
    dp[0] = arr[0]

    # Iterate over dp array, calculating aggregated scores
    for i in range(1, arr_len):
        # Iterate over the range of possible clusters for this item
        #print(f"Calculating dp[{i}]")
        max_elem_score = 0
        cur_clust_max_score = 0
        for j in range(i, max(0, i-k+1)-1, -1):
            #print(f"Considering cluster starting at {j} {i-k+1} {i} {k}")
            # Iterate over the members of the cluster being considered, compute score, consider it
            #print(f"considering: {arr[j]}")
            cur_clust_max_score = max(arr[j], cur_clust_max_score)
            #print(f"cur clust score: {cur_clust_max_score} times {i-j+1}, PLUS {dp[j-1] if j-1 >= 0 else 0}")
            max_elem_score = max((dp[j-1] if j-1 >= 0 else 0) + cur_clust_max_score*(i-j+1), max_elem_score)
        dp[i] = max_elem_score
    return dp[arr_len-1]

"""
def maxSumAfterPartitioningRough(arr, k):
    arr_len = len(arr)
    dp = [0 for _ in range(arr_len)]
    dp[0] = arr[0]

    # Iterate over dp array, calculating aggregated scores
    for i in range(1, arr_len):
        # Iterate over the range of possible clusters for this item
        print(f"Calculating dp[{i}]")
        max_elem_score = 0
        for j in range(max(0, i-k+1), i+1):
            print(f"Considering cluster starting at {j} {i-k+1} {i} {k}")
            # Iterate over the members of the cluster being considered, compute score, consider it
            cur_clust_max_score = 0
            for elem_id in range(j, i+1):
                print(f"considering: {arr[elem_id]}")
                cur_clust_max_score = max(arr[elem_id], cur_clust_max_score)
            print(f"cur clust score: {cur_clust_max_score} times {i-j+1}, PLUS {dp[j-1] if j-1 >= 0 else 0}")
            max_elem_score = max((dp[j-1] if j-1 >= 0 else 0) + cur_clust_max_score*(i-j+1), max_elem_score)
        dp[i] = max_elem_score
    print(dp)
"""

"""
  Faster than 86.40%
  Less memory than 93.95%
"""

def maxSumAfterPartitioning(arr, k):
    arr_len, dp = len(arr), [0] * len(arr)

    for i in range(arr_len):
        max_elem_score = 0
        cur_clust_max_score = 0
        for j in range(i, max(-1, i - k), -1):
            cur_clust_max_score = max(arr[j], cur_clust_max_score)
            max_elem_score = max((dp[(j - 1) % k] if j - 1 >= 0 else 0) + cur_clust_max_score * (i - j + 1),
                                 max_elem_score)
        dp[i % k] = max_elem_score
    return dp[(arr_len - 1) % k]



"""
  19. Remove Nth Node from end of list
  [ Medium ] | [ 38.6% ] -- Solved 24/06/2022
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN:  87.92%
  MEMORY USAGE: 97.95%
"""


def noon(arr, k):
    count = 0
    hm = {}
    for e in arr:
        if e not in hm:
            hm[e] = 0
        elif hm[e] == 3:
            continue
        if e-k in hm and hm[e-k] < 3:
            hm[e] = hm[e] | 1
            hm[e-k] = hm[e-k] | 2
            count += 1
        if e+k in hm and hm[e+k] < 3:
            hm[e] = hm[e] | 2
            hm[e + k] = hm[e + k] | 1
            count += 1
    return count


class Node:
    def __init__(self, letter='a'):
        self.letter = letter
        self.children = [None for _ in range(26)]
        self.end = False

    def addAndGet(self, letter):
        child = self.children[ord(letter)-97]
        if child is None:
            self.children[ord(letter)-97] = child = Node(letter)
        return child


class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        ptr = self.root
        for ch in word:
            ptr = ptr.addAndGet(ch)
        ptr.end = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for ch in word:
            ptr = ptr.children[ord(ch)-97]
            if ptr is None:
                return False
        return ptr.end

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for ch in prefix:
            ptr = ptr.children[ord(ch) - 97]
            if ptr is None:
                return False
        return True

"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    # write your code here
    return '|'.join([s.replace('|', '||') for s in strs])

"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(s):
    strs = []
    is_sep = False
    sep_count = 0
    cs = ''
    for c in s:
        if c == '|':
            if not is_sep:
                is_sep = True
            sep_count += 1
            continue
        if is_sep:
            is_sep=False
            cs += '|'*(sep_count//2)
            if sep_count%2 == 1:
                strs.append(cs)
                cs = ''
            sep_count=0
        cs += c
    strs.append(cs)
    return strs




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    ans = countBits(33)
    ans2 = countBitsRough(33)
    print(ans,"\n",len(ans))
    print([0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,1])
    """
    i = ['Hi there!', 'how are|you||doing|||there?']
    ec = encode(i)
    print(ec)
    dc = decode(ec)
    print(dc)
    print(i)
    # trie = Trie()
    # trie.insert("apples")
    # print(trie.search("apples"))
    #print(noon([1,2,8,5, 5], 0)) [1,1,2,2, 2, 4]
    # {1: 2, 2: 3, 4: 1}
    #print([i for i in test([1,1,2,2,2,4])])
    #print(maxSubArray([-1,1,-3,-2,2,-1,-2,1,2,-3]))
    #print(maxSumAfterPartitioningRough([60803,944497,997590,498033,150561,138570,153226,41113,622181,822694,800277,115626,645658,137059,928394,297438,231177,163449,769246,808442,604124,957600,332557,636426,324832,34085,58274,792852,74280,577167,786935,548388,378009,468173,194692,4264,787409,636893,627810,300623,865415,422759,32705,784116,248487,692081,13592,221155,193259,873781,602722,46711,942154,103237,174444,199004,62018,923809,468472,722938,491426,399914,21857,590369,621475,168235,250082,46937,5906,502955,534299,431492,942630,135032,811501,837998,102081,460524,676687,466534,89827,449525,939156,587723,71590,352189,227615,288550,419637,30495,952893,338146,774358,387564,601329,364223,257403,596289,153399,55681,470354,862,949899,731125,841859,745065,525773,559083,735346,241801,241180,284880,674538,150263,677914,286711,601216,71972,73814,308568,891030,818763,800424,419668,193045,750926,559606,898789,586095,930839,363845,980937,847964,967309,997019,755524,635262,130212,244089,257841,734340,823241,193343,939491,178081,43222,427239,917935,523402,418021,552442,296397,419581,643778,776934,197956,718196,952343,81731,753742,659718,215425,977866,618482,31016,58178,193463,441685,959938,377448,567921,986154,625899,738764,568902,57288,102415,829033,554103,377734,676018,31829,122714,44179,983333,544640,667643,943597,852364,521890,195216,504393,140546,868847,234415,164537,732718,473529,857517,109696,445229,197802,761298,958227,128788,898174,707361,947575,202226,256555,773458,96661,115609,342002,319858,45818,397502,261035,908705,552689,557707,430877,114334,567609,853348,491914,67140,208166,248408,304553,112882,884566,391070,332134,391223,295138,725871,223549,580189,457880,300041,967768,429507,14898,278694,807136,27635,773323,312812,459550,57864,201279,298593,890103,249608,984192,243860,81484,46107,75286,144687,87170,703517,209153,478809,479499,76676,588039,738685,193201,900227,740220,551924,125356,451879,725830,38239,684378,633482,288467,477407,170704,597311,812008,80234,573377,491131,704720,618000,719345,509774,865570,537086,199030,158822,958648,772049,404505,210034,424631,582812,137808,573763,685885,473681,672950,736963,980119,509251,569263,18742,787980,159483,534712,591557,377422,880540,935183,521554,122914,801318,230512,304088,411977,822265,455697,982932,275244,465469,759159,437495,884595,590057,723689,99534,865253,896394,410733,849464,210890,314197,319102,181533,865572,303187,720239,747068,625386,678426,276119,505310,931837,479139,69758,609141,723480,149875,900623,697820,252853,261136,488812,211991,298084,58280,184791,314646,34493,123669,806843,617544,873614,258784,544966,731973,408230,293348,410096,391386,758737,887376,172639,170871,608845,72635,395790,135838,259691,10201,298607,101346,684605,312572,569216,349621,750058,328019,996465,343470,197823,159462,65254,121333,370719,678387,887305,986753,75000,839543,433748,782969,100162,252730,746210,918444,882351,35685,467866,616596,199017,64972,978495,804996,128669,28708,609848,419344,904041,736143,685558,666976,644487,724103,986879,359785,499187,508293,110529,417018,644699,19174,812057,551974,334155,166744,319461,395756,983381,41131,888565,794038,702043,462463,607891,782513,66009,62717,926726,297383,86362,32332,366899,42931,11379,997700,970639,188890,328733,623300,4761,498125,741551,960140,428292], k=311))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
