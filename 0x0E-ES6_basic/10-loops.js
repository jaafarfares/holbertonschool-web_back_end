export default function appendToEachArrayValue(array, appendString) {
  const l = [];
  for (const idx of array) {
    l.push(appendString + idx);
  }
  return l;
}
