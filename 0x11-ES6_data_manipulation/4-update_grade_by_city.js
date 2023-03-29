export default function updateStudentGradeByCity(arr, city, newGrades) {
    return arr.filter((student) => student.location === city).map((student) => {
      let matchinggrades = newGrades.find((grade) => grade.studentId === student.id);
      let grade = matchinggrades ? matchinggrades.grade : 'N/A';
      return { ...student, grade };
    });
  }
