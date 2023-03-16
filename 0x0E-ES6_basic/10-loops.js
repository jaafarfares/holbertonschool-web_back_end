export default function appendToEachArrayValue(array, appendString) {
  const l = [];
  for (let idx of array) {
    var value = idx;
    l.push(appendString + value);
  }
  return l;
}
