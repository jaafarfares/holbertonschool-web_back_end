const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, { encoding: 'utf8' })
    .then((data) => {
      const lines = data.trim().split('\n');
      const students = lines.slice(1).map((line) => line.split(','));

      const numberOfStudents = students.length;
      console.log(`Number of students: ${numberOfStudents}`);

      const fields = {};
      for (const student of students) {
        const field = student[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(student[0]);
      }

      for (const field of Object.keys(fields)) {
        const studentCount = fields[field].length;
        console.log(`Number of students in ${field}: ${studentCount}. List: ${fields[field].join(', ')}`);
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
