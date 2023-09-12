class StudentRepository:

    def __init__(self):
        self.studentList = list()
        # self.studentList = []

    def add(self, student):
        self.studentList.append(student)
        print("학생을 추가하였습니다")

    def findStudentByName(self, name):
        for student in self.studentList:
            if student.name == name:
                return student
        return None

def main():
    from Student import Student
    # from: 모듈파일 import: 모듈 내부의 클래스, 함수, 변수
    sr = StudentRepository()
    sr.add(Student('이동헌', 27))
    sr.add(Student('삼동헌', 28))
    sr.add(Student('사동헌', 29))
    sr.add(Student('오동헌', 30))
    print(sr.studentList)

    print(sr.findStudentByName('이동헌'))

if __name__ == '__main__':
    main()

print('학생저장소 모듈', __name__)