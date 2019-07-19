import squareconnect
from squareconnect.apis.locations_api import *
from squareconnect.apis.transactions_api import *
from time_converter import TimeConverter


class Closing():

    def __init__(self):

        self.time_converter = TimeConverter()
        self.access_token = "EAAAEGo5TJgCAufTCHarwTAnVhcadmlKe_0cgvJNiQ5jLhs-htSp5uS-bO4weW2p"
        self.status = 0

    def retrieve_id(self):

        self.api_instance = LocationsApi()
        self.api_instance.api_client.configuration.access_token = self.access_token

        try:
            self.api_response = self.api_instance.list_locations()
            self.api_locations_list = list(self.api_response.locations)
            self.api_locations_id = self.api_locations_list[0].id

            return self.api_locations_id

        except squareconnect.rest.ApiException as e:
            print('Exception when calling LocationApi->list_locations: %s\n' % e)


    def retrieve_payments(self, cursor):

        self.retrieve_id()
        self.begin_time, self.end_time = self.time_converter.get_time()
        self.api_instance = TransactionsApi()
        self.api_instance.api_client.configuration.access_token = self.access_token

        # try:
        self.api_response = self.api_instance.list_transactions(self.api_locations_id,
                                                                begin_time=self.begin_time, end_time=self.end_time,
                                                                cursor=cursor)
        return self.api_response

        # except squareconnect.rest.ApiException as e:
            # print('Exception when calling TransactionApi->list_payments: %s\n' % e)

    # Check and set the correct time frame.
    def check_payment_log(self):

        if self.status == 0:
            self.get_payment_log()

            if self.log_list[0]['transactions'] == None:
                self.get_payment_log()

    # Enhances the retrieve payment function. Gets all pages of payments in a list.
    def get_payment_log(self):

        self.log_list = []
        try:
            log_retrieved = self.retrieve_payments(cursor=None).to_dict()

            self.log_list.append(log_retrieved)
            self.cursor = log_retrieved['cursor']

            if self.cursor != None:
                while self.cursor != None:
                    log_retrieved = self.retrieve_payments(cursor=self.cursor).to_dict()
                    self.cursor = log_retrieved['cursor']
                    self.log_list.append(log_retrieved)

            return self.log_list

        except AttributeError:
            self.status = 1

    def get_sales_summary(self):

        self.retrieve_id()
        self.check_payment_log()

        total_cash = 0
        total_card = 0
        total_sale = 0
        total_fees = 0
        total_refund = 0
        total_tip = 0

        if self.status == 0:
            if self.log_list[0]['transactions'] != None:
                for i in range(len(self.log_list)):
                    for j in range(len(self.log_list[i]['transactions'])):
                        if self.log_list[i]['transactions'][j]['refunds'] == None:

                            amount = self.log_list[i]['transactions'][j]['tenders'][0]['amount_money']['amount']
                            fee = self.log_list[i]['transactions'][j]['tenders'][0]['processing_fee_money']['amount']
                            tip = self.log_list[i]['transactions'][j]['tenders'][0]['tip_money']

                            total_sale += amount
                            total_fees += fee

                            if self.log_list[i]['transactions'][j]['tenders'][0]['type'] == "CASH":
                                total_cash += amount
                            elif self.log_list[i]['transactions'][j]['tenders'][0]['type'] == "CARD":
                                total_card += amount

                            if tip != None:
                                total_tip += tip['amount']

                        else:
                            amount_refund = self.log_list[i]['transactions'][j]['refunds'][0]['amount_money']['amount']
                            total_refund += amount_refund

            total_net = total_sale - total_fees

            return total_sale, total_net, total_cash, total_card, total_fees, total_refund, total_tip