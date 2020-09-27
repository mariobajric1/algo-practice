//Given an array of a stock's price on any given day, return the maximum profit in K transactions.

//O(nK) time | o(nk) space

maxProfitWithKTransactions = (prices, k) => {
	// if the array is empty, return 0
	if (!prices.length) {
		console.log("0");
	}
	// create profits matrix
	const profits = [];
	//create a row in matrix for each transaction
	for (let t = 0; t < k + 1; t++) {
		const row = new Array(prices.length).fill(0);
		profits.push(row);
	}
	//fill matrix with portential profit with k transactions
	for (let t = 1; t < k + 1; t++) {
		//set initial profits low
		let maxPot = -Infinity;
		// for every day, fill each day potenital profit
		for (let d = 1; d < prices.length; d++) {
			// set the potenital profit to yesterday's profit or the last transaction minus last price
			maxPot = Math.max(maxPot, profits[t - 1][d - 1] - prices[d - 1]);
			//set day's profit to yesterdays or the potential plus current price
			profits[t][d] = Math.max(profits[t][d - 1], maxPot + prices[d]);
		}
	}
	//returns max profit
	console.log(profits[k][prices.length - 1]);
};

maxProfitWithKTransactions([400, 390, 420, 470, 460, 500, 580], 1);

// O(nk)time | O(n) space
maxProfitWithKTransactionsOptimized = (prices, k) => {
	// if the array is empty, return 0

	if (!prices.length) {
		console.log("0");
	}
	//create two consecutive arrays from profits instead of entire matrix
	const evenProfits = new Array(prices.length).fill(0);
	const oddProfits = new Array(prices.length).fill(0);
	//for every transaction starting at the first,
	for (let t = 1; t < k + 1; t++) {
		// sets initial profits low
		let maxPot = -Infinity;
		//variables made to easily iterate later on
		let currentProfits, previousProfits;
		if (t % 2 === 1) {
			currentProfits = oddProfits;
			previousProfits = evenProfits;
		} else {
			currentProfits = evenProfits;
			previousProfits = oddProfits;
		}
		// for every day, the profit is equal to yesterdays profit or the max potential proiit plus todays price.
		for (let d = 1; d < prices.length; d++) {
			maxPot = Math.max(maxPot, previousProfits[d - 1] - prices[d - 1]);
			currentProfits[d] = Math.max(currentProfits[d - 1], maxPot + prices[d]);
		}
	}

	// return max profit
	console.log(
		k % 2 === 0 ? evenProfits[prices.length - 1] : oddProfits[prices.length - 1]
	);
};

maxProfitWithKTransactionsOptimized([400, 390, 420, 470, 460, 500, 580], 1);
