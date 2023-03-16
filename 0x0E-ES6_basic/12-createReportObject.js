export default function createReportObject(employeesList) {
  const allEmployees = {};

  for (const [department, employees] of Object.entries(employeesList)) {
    allEmployees[department] = [...employees];
  }

  return {
    allEmployees,

    getNumberOfDepartments(employees) {
      return Object.keys(employees).length;
    },
  };
}

