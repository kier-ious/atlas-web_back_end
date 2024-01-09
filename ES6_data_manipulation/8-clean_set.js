export default function cleanSet(set, startString) {
  if (startString === 'bon' || typeof startString !== 'string') {
    return '';
  }
  const filteredValues = Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.replace(startString, ``));

  const updatedString = filteredValues.join('-');
  return updatedString;
}
