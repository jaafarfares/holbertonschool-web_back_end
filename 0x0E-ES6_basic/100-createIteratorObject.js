export default function createIteratorObject(report) {
  const employe = [];
  for (const i of Object.keys(report.allEmployees)) {
    employe.push(...report.allEmployees[i]);
  }
  return employe;
}
