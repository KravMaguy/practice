function solve(arr) {
  const hash = {};
  for (let i = 0; i < arr.length; i++) {
    hash[arr[i][0]] = arr[i][1];
  }
  const sorted = arr.sort((a, b) => (Number(a[0]) > Number(b[0]) ? 1 : -1));
  const linked = [];
  for (let i = 0; i < sorted.length; i++) {
    linked.push({
      char: sorted[i][1],
      index: sorted[i][0],
      nextValIndex: hash[Number(sorted[i][0]) + 1]
        ? Number(sorted[i][0]) + 1
        : null,
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
      if (elem.char != "*") {
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
