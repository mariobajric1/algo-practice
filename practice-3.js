// two sum array
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

twoSum = (nums, target) => {
	// create a map
	const comp = {};

	//loop through array
	for (let i = 0; i < nums.length; i++) {
		if (comp[nums[i]] >= 0) {
			//returns answer
			console.log([comp[nums[i]], i]);
		}
		//add to map what 'value' is needed to get sum
		comp[target - nums[i]] = i;
	}
};

twoSum([3, 4, 5, 2], 7);
