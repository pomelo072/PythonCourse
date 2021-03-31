if __name__ == '__main__':
    dic_account = {"John": "123", "Mary": "111", "Tommy": "123456"}
    name = input("请输入用户名:")
    pw = input("请输入密码, 回车确认:")
    if name not in dic_account.keys():
        print("用户名不正确!")
    elif pw != dic_account[name]:
        print("密码不正确!")
    else:
        print("登陆成功")
