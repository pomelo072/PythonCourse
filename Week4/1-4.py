import random as rd
import string


def new_verification():
    key = ""
    for i in range(4):
        key += rd.choice(string.ascii_uppercase)
    print("验证码: " + key)
    return key


def login(db):
    username = input("请输入用户名:")
    valid_password = db.get(username, "用户不存在")
    if valid_password == "用户不存在":
        return valid_password
    currect_key = new_verification()
    valid = input("请输入验证码:").upper()
    if valid != currect_key:
        return "验证码不正确"
    in_password = input("请输入密码:")
    if valid_password != in_password:
        return "密码不正确"
    return "success"


if __name__ == '__main__':
    user_info = {"pomelo": "123456"}
    message = ""
    while message != "success":
        message = login(user_info)
        if message == "success":
            print("登录成功")
            break
        print(message)
