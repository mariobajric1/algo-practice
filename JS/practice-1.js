let arr = [4, 5, 3, 2, 2, 2];

//take in an array of individually numbered socks and return total # of pairs

let pairs = (ar) => {
	let socks = {};
	let pairs = 0;
	for (let i of ar) {
		socks[i] = socks[i] + 1 || 1;
		if (socks[i] % 2 === 0) {
			pairs += 1;
		}
	}
	console.log(pairs);
};

pairs(arr);




let pairs = (ar) => {
	let shoes = {}
	let pairs = 0;
	for(let i of ar) {
		shoes[i] = shoes[i] + 1 || 1;
		if (socks[i] % 2 === 0) {
			pairs += 1;
		}
	}
	console.log(pairs);
}





