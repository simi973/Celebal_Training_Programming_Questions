# PROG 2 : Employee Data (MIS)
employees = [
    {
        'id': 1, 'name': 'John Doe',
        'personal_information': {'gender': 'M', 'age': 28, 'mobile_number': '1234567890', 'additional_mobile_number': None},
        'education_information': {'Degree': 'BE', 'Degree_Stream': 'Computer Science', 'Year_of_passout': 2017, 'total_percentage': 72},
        'skills_information': {'languages': ['Python', 'Java'], 'tools': ['Git', 'Docker']},
        'department_information': {'name_of_dept': 'Development', 'role': 'Developer'}
    },
    {
        'id': 2, 'name': 'Jane Smith',
        'personal_information': {'gender': 'F', 'age': 24, 'mobile_number': '9876543210', 'additional_mobile_number': None},
        'education_information': {'Degree': 'BE', 'Degree_Stream': 'IT', 'Year_of_passout': 2018, 'total_percentage': 85},
        'skills_information': {'languages': ['Python'], 'tools': ['Git', 'Kubernetes']},
        'department_information': {'name_of_dept': 'Development', 'role': 'Developer'}
    },
    {
        'id': 3, 'name': 'Alice Brown',
        'personal_information': {'gender': 'F', 'age': 30, 'mobile_number': '9876543211', 'additional_mobile_number': None},
        'education_information': {'Degree': 'ME', 'Degree_Stream': 'Computer Science', 'Year_of_passout': 2016, 'total_percentage': 80},
        'skills_information': {'languages': ['Java', 'C++'], 'tools': ['Git', 'Jenkins']},
        'department_information': {'name_of_dept': 'Development', 'role': 'Developer'}
    },
    {
        'id': 4, 'name': 'Bob White',
        'personal_information': {'gender': 'M', 'age': 32, 'mobile_number': '9876543212', 'additional_mobile_number': None},
        'education_information': {'Degree': 'BE', 'Degree_Stream': 'IT', 'Year_of_passout': 2015, 'total_percentage': 75},
        'skills_information': {'languages': ['Java', 'Python'], 'tools': ['Docker', 'Git']},
        'department_information': {'name_of_dept': 'Development', 'role': 'Developer'}
    },
    {
        'id': 5, 'name': 'Chris Blue',
        'personal_information': {'gender': 'M', 'age': 40, 'mobile_number': '9876543213', 'additional_mobile_number': None},
        'education_information': {'Degree': 'BE', 'Degree_Stream': 'ECE', 'Year_of_passout': 2010, 'total_percentage': 70},
        'skills_information': {'languages': ['JavaScript', 'Java'], 'tools': ['Git', 'Jenkins']},
        'department_information': {'name_of_dept': 'Testing', 'role': 'QA Engineer'}
    },
    {
        'id': 6, 'name': 'Diana King',
        'personal_information': {'gender': 'F', 'age': 27, 'mobile_number': '9876543214', 'additional_mobile_number': None},
        'education_information': {'Degree': 'BE', 'Degree_Stream': 'Computer Science', 'Year_of_passout': 2019, 'total_percentage': 88},
        'skills_information': {'languages': ['Java', 'Python'], 'tools': ['Docker', 'Kubernetes']},
        'department_information': {'name_of_dept': 'Development', 'role': 'Developer'}
    },
    {
        'id': 7, 'name': 'Eve Green',
        'personal_information': {'gender': 'F', 'age': 23, 'mobile_number': '9876543215', 'additional_mobile_number': None},
        'education_information': {'Degree': 'BE', 'Degree_Stream': 'IT', 'Year_of_passout': 2021, 'total_percentage': 90},
        'skills_information': {'languages': ['Python', 'C++'], 'tools': ['Git', 'Docker']},
        'department_information': {'name_of_dept': 'Operations', 'role': 'DevOps Engineer'}
    },
    {
        'id': 8, 'name': 'Frank Woods',
        'personal_information': {'gender': 'M', 'age': 34, 'mobile_number': '9876543216', 'additional_mobile_number': None},
        'education_information': {'Degree': 'ME', 'Degree_Stream': 'Computer Science', 'Year_of_passout': 2014, 'total_percentage': 78},
        'skills_information': {'languages': ['Java', 'Python'], 'tools': ['Jenkins', 'Docker']},
        'department_information': {'name_of_dept': 'Development', 'role': 'Developer'}
    },
    {
        'id': 9, 'name': 'Grace Hall',
        'personal_information': {'gender': 'F', 'age': 38, 'mobile_number': '9876543217', 'additional_mobile_number': None},
        'education_information': {'Degree': 'BE', 'Degree_Stream': 'IT', 'Year_of_passout': 2012, 'total_percentage': 82},
        'skills_information': {'languages': ['SQL', 'Python'], 'tools': ['Git', 'Jenkins']},
        'department_information': {'name_of_dept': 'Management', 'role': 'Product Manager'}
    },
    {
        'id': 10, 'name': 'Helen Clark',
        'personal_information': {'gender': 'F', 'age': 29, 'mobile_number': '9876543218', 'additional_mobile_number': None},
        'education_information': {'Degree': 'BE', 'Degree_Stream': 'Computer Science', 'Year_of_passout': 2017, 'total_percentage': 86},
        'skills_information': {'languages': ['C++', 'SQL'], 'tools': ['Docker', 'Git']},
        'department_information': {'name_of_dept': 'Testing', 'role': 'QA Engineer'}
    }
]

male = 0
female = 0

below_25 = 0
age_25_35 = 0
above_35 = 0

java_employees = []
python_employees = []
both_employees = []

developers = 0
for emp in employees:
    gender = emp['personal_information']['gender']
    age = emp['personal_information']['age']
    languages = emp['skills_information']['languages']
    role = emp['department_information']['role']

    if gender == 'M':
        male += 1
    else:
        female += 1

    if age < 25:
        below_25 += 1
    elif age <= 35:
        age_25_35 += 1
    else:
        above_35 += 1

    if role == 'Developer':
        developers += 1

    if 'Java' in languages:
        java_employees.append(emp['name'])

    if 'Python' in languages:
        python_employees.append(emp['name'])

    if 'Java' in languages and 'Python' in languages:
        both_employees.append(emp['name'])

print("Gender Distribution Ratio:")
print("Male:", male)
print("Female:", female)
print("\nAge Distribution:")
print("Less than 25:", below_25)
print("25-35:", age_25_35)
print("Above 35:", above_35)
print("\nNumber of Developers:", developers)
print("Employees who know Java:", java_employees)
print("Employees who know Python:", python_employees)
print("Employees who know both Java and Python:", both_employees)