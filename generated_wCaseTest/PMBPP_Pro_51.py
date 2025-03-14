def sort_students_by_total_score(students):
    # Calculate total score for each student and sort based on the criteria
    sorted_students = sorted(
        students,
        key=lambda student: (-sum(score for _, score in student), student[0][0])
    )
    return sorted_students

import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        assert sort_students_by_total_score([[('Alice', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)], [('Bob', 70), ('Science', 85), ('Maths', 80), ('Social sciences', 75)]]) == [[('Alice', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)], [('Bob', 70), ('Science', 85), ('Maths', 80), ('Social sciences', 75)]]
assert sort_students_by_total_score([[('Charlie', 75), ('Science', 80), ('Maths', 70), ('Social sciences', 65)], [('David', 75), ('Science', 80), ('Maths', 70), ('Social sciences', 65)]]) == [[('Charlie', 75), ('Science', 80), ('Maths', 70), ('Social sciences', 65)], [('David', 75), ('Science', 80), ('Maths', 70), ('Social sciences', 65)]]
assert sort_students_by_total_score([[('Eve', 90), ('Science', 95), ('Maths', 85), ('Social sciences', 80)], [('Frank', 90), ('Science', 95), ('Maths', 85), ('Social sciences', 80)]]) == [[('Eve', 90), ('Science', 95), ('Maths', 85), ('Social sciences', 80)], [('Frank', 90), ('Science', 95), ('Maths', 85), ('Social sciences', 80)]]

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)