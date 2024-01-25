def process_authen(self, user, password, login_window):
    if user == "admin" and password == "admin":
        print("correct!")
        self.dash()
        login_window.close()
    else:
        print("incorrect!")
    ### Process connect to BE web here ###