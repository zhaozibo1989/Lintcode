class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # Manacher's Algorithm
        # Time: O(n)
        # Space: O(n)
        
        # if len is 0, no need to explore
        N = len(s)
        if N == 0:
            return s
        
        # construct the string for manacher's algo
        # every char and every gap is a possible center
        A = '@#' + '#'.join(s) + '#$'
        
        # record the single wing length for each center
        wingLen = [0 for _ in range(len(A))]
        
        # at the most begining, the best palindrom is centered
        # at the 0 position and the right bound is at 0 as well
        center, right = 0, 0
        
        for i in range(1, len(A)-1):
            # achieve the mirror position of i by current center
            # center - mirror = i - center
            # mirror = 2*center -i
            mirror = 2*center - i
            
            # treat i as the new center
            # if i is within right bound, i's wing length is at least
            # min(distance between i and right bound, mirror's wing length)
            # i.e. min(right-i, wingLen[mirror])
            if i < right:
                wingLen[i] = min(right-i, wingLen[mirror])
            
            # check if the chars beyond i's wingLen are symmetric 
            # (remember i is the current center)
            # If yes, wingLen of i increase by 1, otherwise stop checking
            while A[i+(wingLen[i]+1)] == A[i-(wingLen[i]+1)]:
                wingLen[i] += 1
            
            # if the i's right bound is beyond current right beyond,
            # update center and right beyond
            if i+wingLen[i] > right:
                center = i
                right = i+wingLen[i]
         
        # get the index with the largest wingLen, and corresponding substring
        index = wingLen.index(max(wingLen))
        substring = ''.join(A[index-wingLen[index]:index+wingLen[index]].split('#'))
        
        return substring