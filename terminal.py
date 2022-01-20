class terminal():
    def __init__(self) -> None:
        pass
    
    def ask_question(self, prompt):
        """Prints prompt and returns answer"""
        return input(prompt)
    def print_response(self, msg):
        """Prints a message"""
        print(msg)

