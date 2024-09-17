const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const header = lines.shift();

      if (!header) {
        throw new Error('Cannot load the database');
      }

      const students = {
        CS: [],
        SWE: [],
      };

      lines.forEach((line) => {
        const [firstname, field] = line.split(',');
        if (field === 'CS') {
          students.CS.push(firstname);
        } else if (field === 'SWE') {
          students.SWE.push(firstname);
        }
      });

      const totalStudents = students.CS.length + students.SWE.length;
      console.log(`Number of students: ${totalStudents}`);
      console.log(`Number of students in CS: ${students.CS.length}. List: ${students.CS.join(', ')}`);
      console.log(`Number of students in SWE: ${students.SWE.length}. List: ${students.SWE.join(', ')}`);
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
