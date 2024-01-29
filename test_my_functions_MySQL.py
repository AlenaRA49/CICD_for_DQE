import pyodbc
import pytest
import pymssql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="TADQA",
  password="Afec06A25@*1bbfA"
)

#cnxn = pyodbc.connect(connectionString)
cursor = mydb.cursor()

#TEST 1 Jobs table. Verify that minimum Salary in the Jobs table not les than 2000
@pytest.mark.xfail
def test_min_salary():
    query = """
       select min(min_salary) from hr.jobs;
       """
    cursor.execute(query)
    rs = cursor.fetchall()
    min_salary = rs[0][0]
    assert int(min_salary) >= 2000

#TEST 2 Jobs table. Verify that there is no Empty Job Titles in Jobs table
def test_job_titles_null():
    query ='''
       select count(*) from hr.jobs where job_title is null or job_title =''
       '''
    cursor.execute(query)
    rs = cursor.fetchall()
    job_titles_null = rs[0][0]
    assert job_titles_null == 0

#TEST 3 Employees table. Verify that there is no Employee with empty Last Name
def test_last_name_null():
    query = """select count(*) from hr.employees where last_name is null"""
    cursor.execute(query)
    rs = cursor.fetchall()
    last_name_null_count = rs[0][0]
    assert last_name_null_count == 0

#TEST 4 Employees table. Verify that employee's salary is within the salary limits for the appropriate Job Title
def test_employee_salary_iscorrect():
    query = '''select count(*) from hr.employees e
    join hr.jobs j on e.job_id=j.job_id
    where e.salary<j.min_salary or e.salary>j.max_salary '''
    cursor.execute(query)
    rs = cursor.fetchall()
    employee_salary = rs[0][0]
    assert employee_salary == 0

#TEST 5 Departments table. Verify that all departments are connected with the specified location
def test_departments_within_the_locations():
    query = '''select count(*) from hr.departments d
    left join hr.locations l on l.location_id = d.location_id
    where d.location_id is null'''
    cursor.execute(query)
    rs = cursor.fetchall()
    departments_locations = rs[0][0]
    assert departments_locations == 0

# TEST 6 Departments table. Verify that Department Name doesn't contain Special symbols
def test_department_name_without_spch():
    query = '''select count(*) 
    from hr.departments
    where UPPER(department_name) not LIKE '%[A-Za-z0-9]%'
    '''
    cursor.execute(query)
    rs = cursor.fetchall()
    department_name_without_spch = rs[0][0]
    assert department_name_without_spch == 0
