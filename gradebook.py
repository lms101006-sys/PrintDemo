# ---------------------------
# 성적 계산 프로그램
# ---------------------------

# 평균을 계산하는 함수
def mean(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

# 평균 점수에 따라 학점을 정하는 함수
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 한 명의 학생 정보를 저장하는 클래스
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())

# 여러 학생의 성적을 관리하는 클래스
class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0
        total = sum(s.average() for s in self.students)
        return total / len(self.students)

# 프로그램의 시작 부분
def main():
    # 학생 생성
    alice = Student("Alice", [90, 85, 92])
    bob = Student("Bob", [70, 75, 68])

    # 성적부 생성 및 학생 추가
    gb = GradeBook()
    gb.add_student(alice)
    gb.add_student(bob)

    # 전체 반 평균 출력
    print("전체 반 평균 점수:", round(gb.class_average(), 2))

    # 각 학생의 평균과 학점 출력
    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")

# 프로그램 실행
if __name__ == "__main__":
    main()