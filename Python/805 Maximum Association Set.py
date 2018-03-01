class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        # Write your code here
        # Python 2
        # Union Find
        # 673ms and 4.58MB
        
        N = len(ListA)  # number of book list
        tot = 0  # initialize book number 
        
        hashMap = {}  # hash map book_name: book_number
        name = []  # book name list
        
        for i in range(N):
            if ListA[i] not in hashMap:    # if the book has not been put in the 
                hashMap[ListA[i]] = tot    # hash map, add it with book_number
                name.append(ListA[i])      # then, update book number.
                tot += 1
            if ListB[i] not in hashMap:
                hashMap[ListB[i]] = tot
                name.append(ListB[i])
                tot += 1
        
        self.father = [i for i in range(tot)]   # initialize father list, each book
                                                # is the father of itself
        
        for i in range(N):
            fatherA = self.find(hashMap[ListA[i]])   # find each book's father
            fatherB = self.find(hashMap[ListB[i]])   # then the father list create
            if fatherA != fatherB:                   # a link among associated books.
                self.father[fatherB] = fatherA       # Each link has a single father
        
        count = [0 for i in range(tot)]  # initialize counts which count books under 
                                         #each father
        countMax, index = 0, 0     # intialize the maximun count and corresponding father index
        for i in range(tot):
            fatherCur = self.find(i)   # for each book, find its father, and update its count
            count[fatherCur] += 1
            if count[fatherCur] > countMax: # update max count and best father 
                countMax = count[fatherCur]
                index = fatherCur
                
        ans = []                       # return answer by putting all the books under
                                        # the best father into the answer
        for i in range(tot):
            if self.find(i) == index:
                ans.append(name[i])
        return ans
                
            
    def find(self,i):                  # define the function to find each book's associated father
            if self.father[i] != i:
                self.father[i] = self.find(self.father[i])
            return self.father[i]
        
        