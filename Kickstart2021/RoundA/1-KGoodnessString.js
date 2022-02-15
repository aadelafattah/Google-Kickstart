const readline = require("readline");

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let t, s, n, k;
let input = [];
rl.question("", (x) => {
	t = 2 * x;
	rl.on("line", (line) => {
		input.push(line);
		t--;
		if (t == 0) {
			rl.close();
			solution();
		}
	});
});

function solution() {
	let i = 0;
	while (i < input.length) {
		n = input[i].split(" ")[0];
		k = input[i].split(" ")[1];
		i++;
		s = input[i];
		i++;
		let count = 0;
		for (let j = 0; j < n / 2; j++) {
			if (s[j] != s[n - j - 1]) {
				count++;
			}
		}
		console.log(`Case #${i / 2}: ${Math.abs(k - count)}`);
	}
}
