export default function createInt8TypedArray(length, position, value) {
  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const array = new DataView(buffer);

  array.setInt8Array(position, value);
  return array;
}
