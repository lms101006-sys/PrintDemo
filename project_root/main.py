# main.py : 프로그램 시작

from models import Student, GradeBook

def main():
    # 학생 객체 생성
    alice = Student("Alice", [90, 85, 92])
    bob = Student("Bob", [70, 75, 68])

    # 성적부 객체 생성
    gb = GradeBook()
    gb.add_student(alice)
    gb.add_student(bob)

    # 결과 출력
    print(f"전체 평균 점수: {round(gb.class_average(), 2)}")

    for s in gb.students:
        print(f"{s.name}의 평균: {s.average():.1f}, 학점: {s.grade()}")

if __name__ == "__main__":
    main()
