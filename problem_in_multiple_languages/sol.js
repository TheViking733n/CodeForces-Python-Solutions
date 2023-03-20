// Programmer: The Viking
// Date: 19.08.2022


var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var arr = [];
rl.question("Enter array: ", function(inp) {
    arr = inp.split(' ').map(Number);
    rl.close();
});

rl.on('close', function() {
    var n = arr.length;
    var freq = {};
    var ind = {};
    for (var i = n - 1; i >= 0; i--) {
        ind[arr[i]] = i;
        if (freq[arr[i]]) {
            freq[arr[i]]++;
        } else {
            freq[arr[i]] = 1;
        }
    }
    var nums = [];
    for (const v in freq) {
        nums.push([-freq[v], ind[v], v]);
    }
    nums = nums.sort(function(a, b) {
        if (a[0] == b[0]) {
            return a[1] - b[1];
        } else {
            return a[0] - b[0];
        }
    });
    var ans = [];
    for (var i = 0; i < nums.length; i++) {
        ans.push(nums[i][2]);
    }
    console.log(...ans);
});
