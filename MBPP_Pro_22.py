def sort_students_by_total_score(students):
    # Calculate total score for each student and sort the list
    students_sorted = sorted(
        students,
        key=lambda student: (-sum(score for _, score in student), student[0][0])
    )
    return students_sorted
