export default function appendToEachArrayValue(array, appendString) {
  for (let idx of array) {
    let value = array;
    array = appendString + value;
  }

  return array;
}
