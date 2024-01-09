export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }
  const filteredValues = Array.from(set)
    .filter((value) => value.startsWith(startString));

  const updatedString = filteredValues.join('-');
  return updatedString;
}
