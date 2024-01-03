export default function appendToEachArrayValue(array, appendString) {
  const newBB = [];
  for (const value of array) {
    array.push(appendString + value);
  }

  return newBB;
}
