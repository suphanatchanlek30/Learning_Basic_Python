from datetime import date

class Account:
    def __init__(self, numID):
        self.number = numID
        self.type = None
        self.interest = 0
        self.balance = 1000  # กำหนดค่า balance เริ่มต้น

    def account_type(self):
        if str(self.number).startswith("1"):
            self.type = "current"
        elif str(self.number).startswith("2"):
            self.type = "saving"

    def interest_rate(self):
        if self.type == "current":
            self.interest = 0
        elif self.type == "saving":
            self.interest = 5
        else:
            raise ValueError("Account type is not defined. Please set the account type first.")
        return self.interest

    def interest_accrued(self):
        # ตรวจสอบว่า account type ถูกตั้งหรือไม่
        if self.type is None:
            self.account_type()
        self.interest_rate()

        current_date = date.today()
        beginning_date = date(current_date.year, 1, 1)
        
        # คำนวณจำนวนวันตั้งแต่ต้นปีจนถึงปัจจุบัน
        days_passed = (current_date - beginning_date).days
        self.interest_accrued_value = self.balance * (days_passed / 365) * self.interest / 100
        return self.interest_accrued_value + self.balance

# สร้าง object
acc = Account(1001)

# ต้องการดู number
print("Account Number:", acc.number)

# ต้องการดู type
acc.account_type()
print("Account Type:", acc.type)

# ต้องการดู interest rate
print("Interest Rate:", acc.interest_rate())

# ต้องการดูดอกเบี้ยสะสม
print("Balance with Interest:", acc.interest_accrued())
