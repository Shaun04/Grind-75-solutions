public class maxProfit{
    public int max(int[] prices) {
        int maxProfit = 0;
        int buy = prices[0];
        for(int i = 1; i < prices.length; i++){
            if(prices[i] > buy){
                if(maxProfit < prices[i] - buy){
                    maxProfit = prices[i] - buy;
                }
            }
            else{
                buy = prices[i];
            }
        }
        return maxProfit;
    }
}
