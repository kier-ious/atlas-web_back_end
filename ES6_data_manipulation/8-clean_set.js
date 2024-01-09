export default function cleanSet(set, startString) {
  const filterSet = Array.from(set).filter((value) => value.startsWith(startString));
  const updatedString = filterSet.append('-');
  return updatedString;
}
