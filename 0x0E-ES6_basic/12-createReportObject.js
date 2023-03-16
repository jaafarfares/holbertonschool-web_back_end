export default function createReportObject(employeesList) {
  return {
    allEmployees: Object.entries(employeesList).reduce(
      (acc, [department, employees]) => {
        if (employees.length > 0) {
          acc[department] = [...employees];
        }
        return acc;
      },
      {}
    ),
    getNumberOfDepartments: function () {
      return Object.keys(this.allEmployees).length;
    },
  };
}

