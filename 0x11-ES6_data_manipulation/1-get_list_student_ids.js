export default function getListStudentIds(arr) {
  if (!Array.isArray(arr)) {
    return [];
  }
  return arr.map((x) => {
    if (x.hasOwnProperty('id')) {
      return x.id;
    }
    return [];
  });
}
