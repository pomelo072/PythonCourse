import datetime as dt


class Medicine:
    def __init__(self, name="", price=0.0, pd="1970-01-01", exp="2100-12-31"):
        self.name = name
        self.price = price
        self.pd = pd
        self.exp = exp

    def get_name(self):
        return self.name

    def get_GP(self):
        start = dt.date.fromisoformat(self.pd)
        end = dt.date.fromisoformat(self.exp)
        gp = end - start
        return "保质期为" + str(gp.days) + "天"


if __name__ == '__main__':
    medicine = Medicine("A", 20, "2020-04-21", "2021-04-20")
    print(medicine.get_name())
    print(medicine.get_GP())
