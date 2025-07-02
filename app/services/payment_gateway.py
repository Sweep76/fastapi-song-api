class CheapPaymentGateway:
    def process_payment(self, total: float) -> bool:
        print(f"Processed with CheapGateway: ${total}")
        return True

class ExpensivePaymentGateway:
    def process_payment(self, total: float) -> bool:
        print(f"Processed with ExpensiveGateway: ${total}")
        return True
