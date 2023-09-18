function countStudents(path) {
    const fs = require('fs');

    if (!fs.existsSync(path)) {
      throw new Error('Cannot load the database');
    }
    const data = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' });

    const rows = data.split('\n');

    let csCount = 0;
    let sweCount = 0;

    const csFirstNames = [];
    const sweFirstNames = [];

    for (let i = 1; i < rows.length; i++) {
      const row = rows[i].trim();

      if (row === '') {
        continue;
      }

      const fields = row.split(',');

      if (fields[3] === 'CS') {
        csCount++;
        csFirstNames.push(fields[0]);
      } else if (fields[3] === 'SWE') {
        sweCount++;
        sweFirstNames.push(fields[0]);
      }
    }

    console.log('Number of students:', csCount + sweCount);
    console.log('Number of students in CS:', csCount, 'List:', csFirstNames.join(', '));
    console.log('Number of students in SWE:', sweCount, 'List:', sweFirstNames.join(', '));
  }
  
  module.exports = countStudents;
  