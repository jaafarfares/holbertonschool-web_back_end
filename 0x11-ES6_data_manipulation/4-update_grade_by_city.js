export default function updateStudentGradeByCity(arr, city, grade) {
    const updatedStudents = arr.map((student) => {
        if (student.location === city) {
          const matchingGrade = grade.find((grade) => grade.studentId === student.id);
          if (matchingGrade) {
            return {
              ...student,
              grade: matchingGrade.grade,
            };
          } else {
            return {
              ...student,
              grade: 'N/A',
            };
          }
        } else {
          return student;
        }
      });
      return updatedStudents;
    }
