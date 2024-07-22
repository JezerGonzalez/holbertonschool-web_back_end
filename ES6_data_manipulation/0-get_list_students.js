export default function getListStudents() {
  const students = [];

  students.push({ id: 1, firstname: 'Guillaume', location: 'San Francisco' });
  students.push({ id: 2, firstname: 'James', location: 'Columbia' });
  students.push({ id: 3, firstname: 'Serena', location: 'San Francisco' });

  return students;
}
