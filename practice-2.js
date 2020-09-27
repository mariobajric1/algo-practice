
//O(nK) time | o(nk) space

maxProfitWithKTransactions = (prices, k) => {
	if (!prices.length) {
		console.log("0");
	}
	const profits = [];
	for (let t = 0; t < k + 1; t++) {
		const row = new Array(prices.length).fill(0);
		profits.push(row);
	}

	for (let t = 1; t < k + 1; t++) {
		let maxPot = -Infinity;
		for (let d = 1; d < prices.length; d++) {
			maxPot = Math.max(maxPot, profits[t - 1][d - 1] - prices[d - 1]);
			profits[t][d] = Math.max(profits[t][d - 1], maxPot + prices[d]);
		}
	}
	console.log(profits[k][prices.length - 1]);
};

maxProfitWithKTransactions([400, 390, 420, 470, 460, 500, 580], 1);



// O(nk)time | O(n) space
maxProfitWithKTransactionsOptimized = (prices, k)  => {
    if ( !price.length){
        console.log("0")
    }
    const evenProfits = new Array(price.length).fill(0);
    const oddProfits = new Array(prices.length).fill(0);
    for ( let t = 1; t < k+1: t++){
        let maxPot = -Infinity;
        let currentProfits, previousProfits;
    }
}