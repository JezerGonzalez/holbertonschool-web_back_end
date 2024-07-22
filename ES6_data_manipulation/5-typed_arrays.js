export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const array = new Int8Array(buffer);

  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }
  array[position] = value;
  return array;
}
