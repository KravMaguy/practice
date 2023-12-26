function solve(arr) {
  const hash = {};
  for (let i = 0; i < arr.length; i++) {
    hash[arr[i][0]] = arr[i][1];
  }

  const linked = [];
  for (const [index, char] of Object.entries(hash)) {
    linked.push({
      char,
      index,
      nextValIndex: hash[Number(index) + 1] ? Number(index) + 1 : null,
    });
  }

  const solutions = [];
  let str = "";
  while (linked.length > 0) {
    const elem = linked.shift();
    if (!elem.nextValIndex) {
      if (str.length > 0) {
        solutions.push(str);
      }
      str = "";
    } else {
      if (elem.char !== "*") {
        str += elem.char;
      }
    }
  }

  return solutions;
}

const input = [
  ["5632583", "*"],
  ["1", "*"],
  ["4", "*"],
  ["2", "a"],
  ["5632585", "*"],
  ["25", "X"],
  ["3", "@"],
  ["5632584", "w"],
];

solve(input);
