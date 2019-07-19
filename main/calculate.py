import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from retrieve_transaction import Closing
from time_converter import TimeConverter



class Calculate:

    def __init__(self, forms_input):
        self.closing = Closing()
        self.drawer = forms_input

        # Get date/time information.
        time_converter = TimeConverter()
        self.date = time_converter.get_time()[0][:10]
        self.year = self.date[:4]
        self.month = self.date[5:7]
        self.day = self.date[8:]

        # Initialize google firebase database instance.
        if firebase_admin._DEFAULT_APP_NAME in firebase_admin._apps:
            pass

        else:
            cred = credentials.Certificate(r'salesinfo-spaceeum-b4ba9f26c833.json')
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def get_square_report(self):
        self.total_sale, self.total_net, self.total_cash, self.total_card, self.total_fees, self.total_refund, self.total_tip = self.closing.get_sales_summary()

        return self.total_sale, self.total_net, self.total_cash, self.total_card, self.total_fees, self.total_refund, \
               self.total_tip

    def closing_summary(self):

        if self.drawer != None:
            self.name = self.drawer['name']
            self.hundred = self.drawer['hundred']
            self.fifty = self.drawer['fifty']
            self.twenty = self.drawer['twenty']
            self.ten = self.drawer['ten']
            self.five = self.drawer['five']
            self.one = self.drawer['one']
            self.quarter = self.drawer['quarter']
            self.dime = self.drawer['dime']
            self.nickel = self.drawer['nickel']
            self.cent = self.drawer['cent']
            self.roll = self.drawer['roll']

        else:
            self.name = ""
            self.hundred = 0
            self.fifty = 0
            self.twenty = 0
            self.ten = 0
            self.five = 0
            self.one = 0
            self.quarter = 0
            self.dime = 0
            self.nickel = 0
            self.cent = 0
            self.roll = 0

        return self.name, self.hundred, self.fifty, self.twenty, \
               self.ten, self.five, self.one, self.quarter, self.dime, \
               self.nickel, self.cent, self.roll

    def get_drawer_report(self):
        self.name, self.hundred, self.fifty, self.twenty, self.ten, self.five, self.one, self.quarter, self.dime, \
        self.nickel, self.cent, self.roll = self.closing_summary()

        if self.hundred == "":
            self.hundred = 0
        if self.fifty == "":
            self.fifty = 0
        if self.twenty == "":
            self.twenty = 0
        if self.ten == "":
            self.ten = 0
        if self.five == "":
            self.five = 0
        if self.one == "":
            self.one = 0
        if self.quarter == "":
            self.quarter = 0
        if self.dime == "":
            self.dime = 0
        if self.nickel == "":
            self.nickel = 0
        if self.cent == "":
            self.cent = 0
        if self.roll == "":
            self.roll = 0

        self.drawer_total = (int(self.hundred) * 10000) + (int(self.fifty) * 5000) + (int(self.twenty) * 2000)\
                         + (int(self.ten) * 1000) + (int(self.five) * 500) + (int(self.one) * 100) + (int(self.quarter) * 25)\
                         + (int(self.dime) * 10) + (int(self.nickel) * 5) + (int(self.cent) * 1) + (float(self.roll) * 100)

        return self.name, self.hundred, self.fifty, self.twenty, self.ten, self.five, self.one, self.quarter, \
               self.dime, self.nickel, self.cent, self.roll, self.drawer_total

    def check_balance(self):
        if (float(self.total_cash) + 20000) == self.drawer_total:
            self.discrepancy = 0
        else:
            self.discrepancy = (self.drawer_total - (self.total_cash + 20000))

        return self.discrepancy


    def display(self):
        self.get_square_report()
        self.get_drawer_report()
        self.check_balance()

        self.output = {
            "Name": self.name,
            "Date": "{}".format(self.date),
            "Net Sale": "${0:.2f}".format(self.total_net / 100),
            "Cash Sale": "${0:.2f}".format(self.total_cash / 100),
            "Card Sale": "${0:.2f}".format(self.total_card / 100),
            "Cash in drawer" : "${0:.2f}".format(self.drawer_total / 100),
            "Total Fees": "${0:.2f}".format(self.total_fees / 100),
            "Total Refunds": "${0:.2f}".format(self.total_refund / 100),
            "Card Tip": "${0:.2f}".format(self.total_tip / 100),
            "Cash Discrepancy": "${0:.2f}".format(self.discrepancy / 100)
        }

        return self.output

    def write_to_database(self, sales_info):
        self.system = self.db.collection("Space.EUm").document("Sales Data").collection(str(self.year))\
            .document(str(self.month)).collection(str(self.day)).document("system")

        self.system.set(sales_info)

        self.system = self.db.collection("Space.EUm").document("Sales Data").collection(str(self.year))\
            .document(str(self.month)).collection(str(self.day)).document("drawer")

        self.system.set(self.drawer)
