export default function getListStudentIds(arr) {
  if (!Array.isArray(arr)) {
    return [];
  }
  return arr.map((x) => {
    if (Object.prototype.hasOwnProperty.call(x, 'id')) {
      return x.id;
    }
    return [];
  });
}
