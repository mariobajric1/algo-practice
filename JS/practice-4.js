// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// addTwoNum = (l1, l2) => {
// 	let s1 = "";
// 	let s2 = "";
// 	let sumstr = "";
// 	for (let i = l1.length - 1; i >= 0; i--) {
// 		s1 += l1[i];
// 	}
// 	for (let i = l2.length - 1; i >= 0; i--) {
// 		s2 += l2[i];
// 	}
// 	sumstr += parseInt(s1) + parseInt(s2);
// 	let ans = Array.from(String(sumstr), Number);
// 	console.log(ans);
// };

// addTwoNum([1, 2, 3], [1, 2, 3, 9, 2]);

var addTwoNumbers = function (l1, l2) {
	let sum = 0;
	let current = new ListNode(0);
	let result = current;

	while (l1 || l2) {
		if (l1) {
			sum += l1.val;
			l1 = l1.next;
		}

		if (l2) {
			sum += l2.val;
			l2 = l2.next;
		}

		current.next = new ListNode(sum % 10);
		current = current.next;

		sum = sum > 9 ? 1 : 0;
	}

	if (sum) {
		current.next = new ListNode(sum);
	}

	console.log(result.next);
};

addTwoNumbers([1, 2, 3], [1, 2, 3, 9, 2]);
