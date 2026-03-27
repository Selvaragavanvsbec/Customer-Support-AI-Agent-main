class QueryAgent:
    def __init__(self, **kwargs):
        pass

    def handle(self, user_input, user_context):
        # Implement logic to handle general queries
        response = self.generate_response(user_input)
        return response

    def generate_response(self, user_input):
        return f"Thank you for reaching out. You asked: '{user_input}'. How can I assist you further?"
