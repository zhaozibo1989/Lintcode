class Solution:
    """
    @param rating: the rating of the movies
    @param G: the realtionship of movies
    @param S: the begin movie
    @param K: top K rating 
    @return: the top k largest rating moive which contact with S
    """
    def topKMovie(self, rating, G, S, K):
        # Write your code here
        # Python 3

        from heapq import heappush, heappop # import heap operations 
        
        mUnchecked = set(G[S])   #this set stores the movies to be checked
        mChecked = set() #this set stores the movies that has been checked
        count = 0  # the size of the moive list candidates
        heap = []  # use heap to store the highest rated K movies
        
        while mUnchecked:
            M = mUnchecked.pop()  # pop out a movie from unchecked set
            if count < K:    # if the heap is smaller than K, push it in
                heappush(heap, (rating[M],M))
                count += 1
            else:
                minRating = heap[0][0]   # otherwise, we chech if the rating
                if minRating < rating[M]: # is higher than the lowest rated movie in the heap
                    heappop(heap) #if yes, pop the lowest one, and push in the current one
                    heappush(heap, (rating[M],M))
            mChecked.add(M)   # add the movie into the checked set
            
            # the add the movies related to this one into unchecked set
            # if it is already there or has been checked, skip it
            for Mrel in G[M]:
                if Mrel != S and Mrel not in mChecked and Mrel not in mUnchecked:
                    mUnchecked.add(Mrel)
        
        #print(heap)
        return [heap[i][1] for i in range(K)]
        
                    