import hashlib

salt = "SaltRandomizer"
db_txt_file_pth = '/path/to/your/database/db.txt'

while True:    
    def menu():
        while True:
            print("[0] Register")
            print("[1] Login")
            print("[2] Exit \n")
            num = input("Pick a number bra: \n")
            if num == "0":
                register()
                break
            elif num == "1":
                login()
                break
            elif num == "2":
                exit()
                break
            else:
                print("-" * 50)
                print("Right, I think you are f*ckin' loserboi...") 
                print("-" * 50)       

    def sha256hasher(plain):
        x = hashlib.sha256()
        x.update(plain.encode('utf-8'))
        return x.hexdigest()

    def register():
        p_text_username = input("Username: ")
        p_text_passwd = input("Password: ")
        writeDB(p_text_username,p_text_passwd)
        print("-" * 100)

    def login():
        p_text_username_login = input("Username: ")
        p_text_passwd_login = input("Password: ")
        readDB(p_text_username_login,p_text_passwd_login)

    def writeDB(username,passwd):
        file = open(db_txt_file_pth, "a")
        file.write(username + ":" + (sha256hasher(salt + username + salt[:5] + passwd + passwd[:1] + salt))[:59] + "\n")

    def readDB(username,passwd):
        query = (username + ":" + sha256hasher((salt + username + salt[:5] + passwd + passwd[:1] + salt))[:59]+ "\n")
         
        line_counter = 0
        incor = 0
        file = open(db_txt_file_pth,"r")
        for line in file:
            line_counter += 1
            if query in line:
                incor = 1
                break
        if incor == 0:
            print("-" * 50)
            print("\n Username or password incorrect. \n")
            print("-" * 50)
        else:
            print("-" * 50)
            print("\n Logged successful. \n")   
            print("-" * 50)
    menu()
