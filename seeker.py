class seeker():
    def __init__(self) -> None:
        self.prompt = "Please enter a number 1-100: "
        self.response = 0
        self.response_cold = "You are cold!"
        self.response_colder = "You are colder!"
        self.response_coldest = "You are Freezing!"
        self.response_Warm = "You are warm!"
        self.response_warmmer = "You are getting Warmmer!"
        self.response_warmmest = "You are Burning Up!"
        self.response_caught = "You Found me!  You Win!"
        self.response_loss = "I have escaped!  You Lose!"
    def report(self, switch):
        """reports back the response based on the input."""
        if switch == 1:
            return self.response_cold
        elif switch == 2:
            return self.response_colder
        elif switch == 3:
            return self.response_coldest
        elif switch == 4:
            return self.response_Warm
        elif switch == 5:
            return self.response_warmmer
        elif switch == 6:
            return self.response_warmmest
        elif switch == 7:
            return self.response_caught
        elif switch == 8:
            return self.response_loss
    
    def set_response(self, answer):
        self.response = answer
