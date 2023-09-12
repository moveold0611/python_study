from basic.userManagement.config.DataBaseConfig import DataBaseConfig, pymysql
class UserRepository:

    @staticmethod
    def saveUser(user = None):
        connection = DataBaseConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f"""
insert into user_tb
values(0, %s, %s, %s, %s)
"""
        insertCount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
        # cursor를 활용해 표현식으로 ``를 포함하여 삽입한다.
        connection.commit()
        return insertCount