class Error:
    def __init__(self, msg:str="Default message", code:int=1):
        self.msg = msg
        self.code = code
    def __str__(self):
        return(f"Error: {self.msg}")

UserNotFoundError = Error("User not found")
UserAlreadyExistsError = Error("User already exists")

if __name__ == "__main__":
    print(UserNotFoundError)