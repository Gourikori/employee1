from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Gouri\n"
        "Employee ID: 31204\n"
        "Department: IT\n"
        "Salary: 55000"
    )
    assert employee_details("Gouri", "31204", "IT", 55000) == expected_output