** start of main.py **

class Category:
    def __init__(self, name):
        self.name=name
        self.ledger=[]

    def deposit(self,amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
       
    def withdraw(self,amount, description=""):
        if self.check_funds(amount):  
 # the check_funds method is gonna be defined later, it is used to check if there is enough money
            self.ledger.append({'amount': -amount, 'description': description} )
            return True
        else:
            return False
    
    def get_balance(self):
        total=0
        for item in self.ledger:
            total+=item["amount"]
        return total

    def transfer(self,amount, other_Category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {other_Category.name}")
            other_Category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        
    def check_funds(self,amount):
        if amount<=self.get_balance():
            return True
        else:
            return False 

    def __str__(self):
        title=f"{self.name:*^30}\n"
        items=""
        for entry in self.ledger:
            descrpt=entry["description"][:23].ljust(23)
            amnt=f"{entry['amount']:.2f}".rjust(7)
            items+=f"{descrpt}{amnt}\n"
        total= f"Total: {self.get_balance():.2f}"
        return title+items+total



def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Step 1: Calculate total spent per category (only withdrawals)
    spent = []
    for cat in categories:
        cat_spent = sum(-entry["amount"] for entry in cat.ledger if entry["amount"] < 0)
        spent.append(cat_spent)

    total_spent = sum(spent)

    # Step 2: Calculate percentages rounded down to nearest 10
    percentages = [int(s / total_spent * 100) // 10 * 10 for s in spent]

    # Step 3: Build the chart line by line
    chart = ""
    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "|"
        for p in percentages:
            line += " o " if p >= i else "   "
        line += " "
        chart += line + "\n"

    # Step 4: Horizontal line under the bars
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Step 5: Print category names vertically
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        if i < max_len - 1:
            line += "\n"
        chart += line

    return title + chart


** end of main.py **

