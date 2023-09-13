from basic.userManagement.config.DataBaseConfig import DataBaseConfig, pymysql
class UserRepository:

    @staticmethod
    def saveUser(user = None):
        connection = DataBaseConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = """
        insert into user_tb 
        values(0, %s, %s, %s, %s)
        """
        insertCount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
        # cursor를 활용해 표현식으로 ``를 포함하여 삽입한다.
        connection.commit()
        return insertCount

    @staticmethod
    def getUserAll():
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql ="""
            select user_id as userId, username, password, name, email 
            from user_tb
            """
            cursor.execute(sql)
            rs = cursor.fetchall()
            return rs
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def getUserByUsername(username = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            select 
                user_id as userId,
                username,
                password,
                name,
                email 
            from
                user_tb 
            where
                username = %s
            """
            cursor.execute(sql, username)
            rs = cursor.fetchone()
            return rs
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def updateUser(user = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            update 
                user_tb
            set
                password = %s,
                name = %s,
                email = %s
            where 
                user_id = %s ;
            """
            updateCount = cursor.execute(sql, (user.password, user.name, user.email, user.userId))
            connection.commit()
            return updateCount
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def deleteUser(userId):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = f"""
            delete 
                from 
                    user_tb 
                where 
                    user_id = {userId};
            """
            deleteCount = cursor.execute(sql)
            connection.commit()
            return deleteCount
        except Exception as e:
            print(e)
            return None