package com.barosanu;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

public class EmployeeListTest {

    private EmployeeList employeeList;
    private Employee employee1;
    private Employee employee2;
    private Employee employee3;

    @BeforeEach
    void setUp() {
        employeeList = new EmployeeList();
        employee1 = new Employee("John Doe", 35, 55000);
        employee2 = new Employee("Jane Smith", 42, 65000);
        employee3 = new Employee("Bob Johnson", 28, 60000);
    }

    @Test
    void testAddEmployee() {
        employeeList.addEmployee(employee1);
        assertEquals(1, employeeList.getEmployeeList().size());
        assertTrue(employeeList.getEmployeeList().contains(employee1));
    }

    @Test
    void testRemoveEmployee() {
        employeeList.addEmployee(employee1);
        employeeList.addEmployee(employee2);
        employeeList.removeEmployee(employee1);
        assertEquals(1, employeeList.getEmployeeList().size());
        assertFalse(employeeList.getEmployeeList().contains(employee1));
        assertTrue(employeeList.getEmployeeList().contains(employee2));
    }

    @Test
    void testGetEmployeeNames() {
        employeeList.addEmployee(employee1);
        employeeList.addEmployee(employee2);
        String[] expectedNames = {"John Doe", "Jane Smith"};
        assertArrayEquals(expectedNames, employeeList.getEmployeeNames());
    }

    @Test
    void testGetEmployeeNamesWithStreams() {
        employeeList.addEmployee(employee1);
        employeeList.addEmployee(employee2);
        String[] expectedNames = {"John Doe", "Jane Smith"};
        assertArrayEquals(expectedNames, employeeList.getEmployeeNamesWithStreams());
    }

    @Test
    void testGetEmployeesSortedByAge() {
        employeeList.addEmployee(employee1);
        employeeList.addEmployee(employee2);
        employeeList.addEmployee(employee3);
        List<Employee> sortedList = employeeList.getEmployeesSortedByAge();
        assertEquals(3, sortedList.size());
        assertEquals(employee3, sortedList.get(0));
        assertEquals(employee1, sortedList.get(1));
        assertEquals(employee2, sortedList.get(2));
    }

    @Test
    void testGetEmployeesWithSalaryGreaterThan() {
        employeeList.addEmployee(employee1);
        employeeList.addEmployee(employee2);
        employeeList.addEmployee(employee3);
        List<Employee> filteredList = employeeList.getEmployeesWIthSalaryGreaterThan(62000);
        assertEquals(1, filteredList.size());
        assertTrue(filteredList.contains(employee2));
    }

    @Test
    void testEmptyList() {
        assertTrue(employeeList.getEmployeeList().isEmpty());
        assertEquals(0, employeeList.getEmployeeNames().length);
        assertEquals(0, employeeList.getEmployeeNamesWithStreams().length);
        assertTrue(employeeList.getEmployeesSortedByAge().isEmpty());
        assertTrue(employeeList.getEmployeesWIthSalaryGreaterThan(0).isEmpty());
    }
}
