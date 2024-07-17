export default function appendToEachArrayValue(array, appendString) {
  for (const value of array) {
    array.push(appendString + value);
  }
  return array;
}
