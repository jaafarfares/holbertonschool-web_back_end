const fs = require('fs');

function countStudents(path) {
  let data;

  try {
    data = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' });
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.trim().split('\n');
  const students = lines.slice(1).map((line) => line.split(','));

  const numberstudents = students.length;
  console.log(`Number of students: ${numberstudents}`);

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
}

module.exports = countStudents;
