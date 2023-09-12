class UserInfo:

    #cls변수(클래스 변수 == static)
    adminUser = {
        'username': 'root',
        'password': '1q2w3e4r'
    }

    # 변수 선언을 일반적으로 init안에서 한다
    def __init__(self):
        self.adminUser = {
            'username': 'user1',
            'password': '1234'
        }

    @classmethod
    def showAdminUser(cls):
        print('[showAdminUser]')
        print(cls.adminUser)

    # 이렇게 작성하면 이하의 변수들을 사용한다.


class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.name = None
        self.email = None

    @staticmethod
    def showUserClassInfo():
        print('그냥그냥 실행실행 메소드')

if __name__ == '__main__':
    userInfo = UserInfo()
    print(userInfo.adminUser)
    print(UserInfo.adminUser)

    userInfo.showAdminUser()
    UserInfo.showAdminUser()

    User.showUserClassInfo()