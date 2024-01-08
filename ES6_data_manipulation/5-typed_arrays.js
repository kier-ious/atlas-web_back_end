export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new TypeError('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const Int8Array = new Int8Array(buffer);
  Int8Array[position] = value;

  return buffer;
}
