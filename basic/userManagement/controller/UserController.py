from basic.userManagement.util.ResponseEntity import ResponseEntity
class UserController:

    @staticmethod
    def registerUser(user = None):
        from basic.userManagement.repository.UserRepository import UserRepository
        responseBody = bool(UserRepository.saveUser(user))
        return ResponseEntity(body=responseBody)