export default function createEmployeesObject(departmentName, employees) {
  const EmployeesObject = {};
  employeesObject[departmentName] = employees;

  return employeesObject;
}
