export default function cleanSet(set, startString) {
  const arrayFromSet = Array.from(set);
  const filterSet = arrayFromSet.filter((value) => value.startsWith(startString));
  const updatedString = filterSet.join('-');
  return updatedString;
}
