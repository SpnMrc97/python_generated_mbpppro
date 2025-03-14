def sort_students_by_total_score(students):
    # Calculate total score for each student and sort based on the criteria
    sorted_students = sorted(
        students,
        key=lambda student: (-sum(score for _, score in student), student[0][0])
    )
    return sorted_students
