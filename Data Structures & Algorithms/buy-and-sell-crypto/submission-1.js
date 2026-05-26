class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let s=0; let e = 1;
        let max = 0;

        while(e < prices.length){
            if(prices[s] < prices[e]){
                let profit = prices[e] - prices[s];
                max = Math.max(profit, max)
            }else{
                s = e
            }
            e++
        }
        return max;
    }
}
