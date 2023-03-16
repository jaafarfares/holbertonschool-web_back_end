export default function appendToEachArrayValue(array, appendString) {
  const l = [];
  for (let idx of array) {
    l.push(appendString + idx);
  }
  return l;
}
