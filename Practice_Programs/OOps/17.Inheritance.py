#17. Member and PremiumMember

class Member:
    def __init__(self, name):
        self.name = name

    def benefits(self):
        return "Basic access"

class PremiumMember(Member):
    def benefits(self):
        return "Premium access + free delivery"

pm = PremiumMember("Akash")
print(pm.benefits())