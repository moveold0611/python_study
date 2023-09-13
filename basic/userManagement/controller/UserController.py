from basic.userManagement.util.ResponseEntity import ResponseEntity
from basic.userManagement.repository.UserRepository import UserRepository
class UserController:

    @staticmethod
    def registerUser(user = None):
        responseBody = bool(UserRepository.saveUser(user))
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getAllUser():
        responseBody = UserRepository.getUserAll()
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getUserByUsername(username = None):
        responseBody = UserRepository.getUserByUsername(username)
        return ResponseEntity(body=responseBody)

    @staticmethod
    def updateUserByUserId(user = None):
        responseBody = bool(UserRepository.updateUser(user))
        return ResponseEntity(body=responseBody)

    @staticmethod
    def deleteUserByUserId(userId = None):
        responseBody = bool(UserRepository.deleteUser(userId))
        return ResponseEntity(body=responseBody)