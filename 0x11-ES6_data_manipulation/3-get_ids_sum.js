export default function getStudentIdsSum(arr) {
  const ids = arr.map((student) => student.id);
  const sum = ids.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  return sum;
}
