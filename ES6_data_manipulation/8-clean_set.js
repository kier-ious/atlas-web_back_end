export default function cleanSet(set, startString) {
  const arrayFromSet = Array.from(set);
  const filteredValues = arrayFromSet.filter((value) => value.startsWith(startString));
  const updatedString = filteredValues.join('-');
  return updatedString;
}
