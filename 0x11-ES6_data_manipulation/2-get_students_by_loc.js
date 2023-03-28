export default function getStudentsByLocation(arr, city) {
  return arr.filter((student) => {
    return student.location === city;
  });
}
