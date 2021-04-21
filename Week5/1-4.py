import datetime as dt


class Account:
    def __init__(self, name, money=0.0, record=None):
        self.name = name
        self.money = money
        if record is None:
            self.record = []
        else:
            self.record = record

    def __str__(self):
        return "您的账户名:"+self.name+"\n您的余额:"+str(self.money)

    def transaction(self, tips, bus=0.0, date=None, currency=None):
        if date == "":
            date = dt.date.today().strftime("%Y/%m/%d")
        if currency == "":
            currency = "人民币"
        if (bus > 0 and tips == "转入") or (bus < 0 and tips in ["消费", "网转"]):
            if self.money + bus < 0:
                print("交易失败")
            else:
                self.money += bus
                now_money = self.money
                new_record = [date, tips, bus, currency, now_money]
                self.record.append(new_record)
                print("交易成功")
        else:
            print("交易失败")

    def print_record(self):
        print("交易日期\t摘要\t金额\t币种\t余额")
        for record in self.record:
            print("{}\t{}\t{}\t{}\t{}".format(record[0], record[1], record[2], record[3], record[4]))


if __name__ == '__main__':
    print("功能列表:\n1. 开户\n2. 消费或转载\n3. 打印账单\n0. 退出程序")
    bank = {}
    select = ""
    while select != "0":
        select = input("选择功能:")
        if select == "1":
            name = input("请输入开户账户名:")
            flag = bank.get(name, 0)
            if flag == 0:
                account = Account(name)
                bank[name] = account
                print("您的账户信息:\n", account)
            else:
                print("已有同名账户, 请重试")
        if select == "2":
            name = input("请输入账户名:")
            account = bank.get(name, 0)
            if account == 0:
                print("不存在账户, 请先开户")
            else:
                account.transaction(input("请输入消费类别:"), float(input("消费金额:")),
                                    input("消费日期(yyyy/mm/dd),直接回车默认今天:"),
                                    input("币种(直接回车默认人民币):"))
        if select == "3":
            name = input("请输入账户名:")
            account = bank.get(name, 0)
            if account == 0:
                print("不存在账户, 请先开户")
            elif len(account.record) == 0:
                print("没有任何记录")
            else:
                account.print_record()
