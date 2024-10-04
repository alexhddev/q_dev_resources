package com.barosanu;

import java.util.ArrayList;
import java.util.List;

public class EmployeeList {

    private List<Employee> employeeList = new ArrayList<>();

    public void addEmployee(Employee employee) {
        employeeList.add(employee);
    }

    public void removeEmployee(Employee employee) {
        employeeList.remove(employee);
    }

    public String[] getEmployeeNames() {
        String[] names = new String[employeeList.size()];
        for (int i = 0; i < employeeList.size(); i++) {
            names[i] = employeeList.get(i).getName();
        }
        return names;
    }

    public String[] getEmployeeNamesWithStreams() {
        return employeeList.stream()
                .map(Employee::getName)
                .toArray(String[]::new);
    }

    public List<Employee> getEmployeeList() {
        return employeeList;
    }

    public List<Employee> getEmployeesSortedByAge(){
        return employeeList.stream()
                .sorted((e1, e2) -> Integer.compare(e1.getAge(), e2.getAge()))
                .toList();
    }

    public List<Employee> getEmployeesWIthSalaryGreaterThan(double salary) {

        return employeeList
                .stream()
                .filter(e -> e.getSalary() > salary)
                .toList();

    }
    
}
