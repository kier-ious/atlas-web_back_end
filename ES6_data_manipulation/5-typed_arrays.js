export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new TypeError('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const Int8 = new Int8Array(buffer);
  Int8[position] = value;
  const DataView = new DataView(buffer);

  return DataView(buffer);
}
