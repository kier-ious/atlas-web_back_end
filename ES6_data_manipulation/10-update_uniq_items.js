export default function updateUniqueItems(mapForFood) {
  if (!(mapForFood instanceof Map)) {
    throw new TypeError('Cannot process');
  }
  for (const [item, quantity] of mapForFood) {
    if (quantity === 1) {
      mapForFood.set(item, 100);
    }
  }
}
