const MAX = 5;

export const  weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    const count = weakMap.get(endpoint);
    weakMap.set(endpoint, count +1);
    if (count >= MAX) {
      throw new Error('Endpoint load is high');
    }
  }
  weakMap.set(endpoint, 1);
}
