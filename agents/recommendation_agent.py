import json

class RecommendationAgent:
    def __init__(self, **kwargs):
        # Initialize as a plain class for the mockup
        # Load product data
        with open('data/sample_data.json', 'r') as f:
            self.product_data = json.load(f)["products"]

    def handle(self, user_input, user_context):
        # Implement logic to provide product recommendations
        recommendations = self.generate_recommendations(user_input)
        return recommendations

    def generate_recommendations(self, user_input):
        # Simple keyword matching for demonstration
        keywords = user_input.lower().split()
        matched_products = [p for p in self.product_data if any(k in p['name'].lower() for k in keywords)]
        if matched_products:
            product_names = ', '.join([p['name'] for p in matched_products])
            return f"We recommend the following products based on your interest: {product_names}."
        else:
            return "Sorry, we couldn't find any products matching your interests."
