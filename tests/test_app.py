import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
import app


class TestStudentApp(unittest.TestCase):

    def test_student_name(self):
        self.assertIn("Name: Nurasyl", app.message)

    def test_student_group(self):
        self.assertIn("Group: IT2-2308", app.message)

    def test_student_id(self):
        self.assertIn("Student ID: 37841", app.message)

    def test_application_message(self):
        self.assertIn("Application is running successfully!", app.message)


if __name__ == "__main__":
    unittest.main()
