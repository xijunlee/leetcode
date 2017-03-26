class Solution(object):
    '''My solution
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
       
        f = []
        for i in range(len(prices)):
            f.append(0)
        for i in range(1,len(prices)):
            minP = 0x7fffffff
            for j in range(0,i):
                minP = min(minP,prices[j])
            f[i] = max(f[i-1],prices[i]-minP)
        if len(prices)-1 >= 0:
            return f[len(prices)-1]
        else:
            return 0
    '''
    '''
    Standard solution
    '''
    def maxProfit(prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit