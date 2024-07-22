export default function updateStudentGradeByCity(list, city, newGrades) {
  return list
    .filter((student) => student.location === city)
    .map((student) => {
      const grades = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grades: grades ? grades.grade : 'N/A',
      };
    });
}
