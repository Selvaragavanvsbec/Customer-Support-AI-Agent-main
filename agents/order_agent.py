class OrderAgent:
    def __init__(self, **kwargs):
        pass

    def handle(self, user_input, user_context):
        response = self.process_order_query(user_input)
        return response

    def process_order_query(self, user_input):
        return f"Regarding your order query: '{user_input}', our team is looking into it and will update you shortly."
