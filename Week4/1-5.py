def Add_people(dic):
    name = input("请输入新增姓名:")
    edit_name = dic.get(name, "no")
    if edit_name != "no":
        goOn = input("已存在该联系人. 更新信息按y, 按其他键退出 ")
        if goOn == "y":
            number = input("请输入更新的号码:")
            dic[name] = number
            return "更新成功"
    else:
        number = input("请输入新增号码:")
        dic[name] = number
        return "添加成功"


def Search_number(dic):
    name = input("请输入查询的名字:")
    temp = dic.get(name, "该联系人不存在")
    if temp != "该联系人不存在":
        return "联系人 " + name + " 的电话为: " + temp
    else:
        return temp


def Delete_number(dic):
    name = input("请输入要删除的联系人姓名:")
    temp = dic.pop(name, "该联系人不存在")
    if temp != "该联系人不存在":
        return "已删除联系人 " + name
    else:
        return temp


if __name__ == '__main__':
    print("a. 新增联系人\nb. 查询联系人\n"
          "c. 删除联系人\nd. 退出程序:")
    a = input("请输入功能序号:\n")
    account = {}
    while a != "d":
        if a == "a":
            print(Add_people(account))
        elif a == "b":
            print(Search_number(account))
        elif a == "c":
            print(Delete_number(account))
        else:
            print("错误!请重新输入")
        a = input("请输入功能序号:\n")
