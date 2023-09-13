import pandas as pd
from basic.userManagement.controller.UserController import UserController
from basic.userManagement.entity.User import User
class UserView:

    @staticmethod
    def register():
        print('사용자 등록 화면')
        username = input('사용자 이름 >>>')
        if username == "":
            print('아이디를 입력해주세요.')
            return
        password = input('비밀번호 >>>')
        if password == "":
            print('비밀번호를 입력해주세요.')
            return
        name = input('이름 >>>')
        email = input('이메일 >>>')

        response = UserController.registerUser(User(
            username=username,
            password=password,
            name=name,
            email=email
        ))

        if not response.__dict__.get("body"):
            print("데이터를 추가하는 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")

    @staticmethod
    def getAllUserList():
        response = UserController.getAllUser()
        if not bool(response.body):
            print('조회할 데이터가 없습니다.')
        else:
            print(pd.DataFrame(response.body))

        if not response.__dict__.get("body"):
            print("데이터를 조회 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")
        return pd.DataFrame(response.body)

    @staticmethod
    def selecter():
        username = input('검색할 username을 입력하세요 >>> ')
        if username == "":
            print('조회 취소')
            return
        response = UserController.getUserByUsername(username)
        if not bool(response.body):
            print('일치하는 user가 없습니다.')
            return
        print(pd.Series(response.body))
        if not response.__dict__.get("body"):
            print("데이터를 조회 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")

    @staticmethod
    def updater():
        df = UserView.getAllUserList()
        rs = UserController.getAllUser()
        print('사용자 업데이트 화면')
        userId = input('수정할 사용자ID >>>')
        if userId == "":
            print('수정 취소')
            return
        index = df.index[df["userId"] == int(userId)].values[0]
        user = UserView.showUpdateMenu(rs.body[index])
        print(user)


        response = UserController.updateUserByUserId(User(
            userId=userId,
            username=user.username,
            password=user.password,
            name=user.name,
            email=user.email
        ))

        if not response.__dict__.get("body"):
            print("데이터를 수정하는 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")
        else:
            print("데이터 수정 성공")

    @staticmethod
    def showUpdateMenu(oldUser):
        user = User(
            userId=oldUser.get('userId'),
            username=oldUser.get('username'),
            password=oldUser.get('password'),
            name=oldUser.get('name'),
            email=oldUser.get('email')
        )
        print(user)
        while True:
            df = pd.DataFrame([oldUser, user.__dict__], index=["수정 전", "수정 후"])
            print(df)
            print("=" * 100)
            print('1. password 수정')
            print('2. name 수정')
            print('3. email 수정')
            print('4. 저장')
            print('5. 취소')
            select = input('메뉴 선택 >>> ')

            if select == '5':
                return None
            elif select == '4':
                return user
            elif select == '3':
                email = input('이메일 변경 >>> ')
                if not UserView.checkInputValid(oldUser.get('email'), email):
                    continue
                user.email = email
                continue
            elif select == '2':
                name = input('이름 변경 >>> ')
                if not UserView.checkInputValid(oldUser.get('name'), name):
                    continue
                user.name = name
                continue
            elif select == '1':
                password = input('패스워드 변경 >>> ')
                if not UserView.checkInputValid(oldUser.get('password'), password):
                    continue
                checkPassword = input('패스워드 확인 >>> ')
                if checkPassword != password:
                    print("비밀번호가 일치하지 않습니다.")
                    continue
                else:
                    user.password=password
                    continue

            else:
                print("선택하신 번호는 등록되지 않은 메뉴입니다.")
                print()
            return None

    @staticmethod
    def checkInputValid(oldValue, value):
        if not bool(value):
            print("공백일 수 없습니다.")
            return False
        elif oldValue == value:
            print("기존의 정보와 동일합니다.")
            return False
        else:
            return True

    @staticmethod
    def deleter():
        df = UserView.getAllUserList()
        rs = UserController.getAllUser()
        print('뒤로가기: q')
        userId = input('삭제할 userId를 입력하세요 >>> ')
        if userId == "q":
            print('삭제 취소')
            return
        index = df.index[df["userId"] == int(userId)].values[0]
        selectedUser = rs.body[index]
        print('정말로 삭제하시려면 username과 password를 입력하세요')
        username = input('삭제할 username과 입력하세요 >>> ')
        if selectedUser.get('username') != username:
            print("아이디가 일치하지 않습니다.")
            return
        password = input('삭제할 password 입력하세요 >>> ')
        if selectedUser.get('password') != password:
            print("아이디가 일치하지 않습니다.")
            return
        response = UserController.deleteUserByUserId(userId)
        
        if not response.__dict__.get("body"):
            print("데이터를 삭제 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")
        else:
            print("데이터 삭제 성공")