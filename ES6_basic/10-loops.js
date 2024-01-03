export default function appendToEachArrayValue(array, appendString) {
  const newBB = [];
  for (const value of array) {
    newBB.push(appendString + value);
  }

  return newBB;
}
