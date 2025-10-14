# gradebook/cli.py
# ----------------------
"""명령행 인터페이스 (CLI)"""

from .models import Student, GradeBook
from .csvio import import_students_from_csv

def run_cli():
    print("GradeBook CLI 실행 중...")

    # CSV에서 학생 목록 불러오기 (예: students.csv)
    try:
        students = import_students_from_csv("students.csv")
        print("파일에서 학생 목록을 불러왔습니다.")
    except FileNotFoundError:
        print("⚠️ 'students.csv' 파일이 없습니다. 기본 데이터를 사용합니다.")
        students = [
            Student("Alice", [90, 85, 92]),
            Student("Bob", [70, 75, 68]),
            Student("Charlie", [88, 93, 79]),
        ]

    gb = GradeBook()
    for s in students:
        gb.add_student(s)

    print(f"\n전체 평균 점수: {gb.class_average():.2f}")
    for s in gb.students:
        print(f"{s.name}: 평균 {s.average():.1f}, 학점 {s.grade()}")
