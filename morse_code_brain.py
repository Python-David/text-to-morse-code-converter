class MorseCodeBrain:
    def __init__(self, rules):
        self.ans = None
        self.rules = rules

    def validate(self, text):
        rejected_letters = []
        for x in text.lower():
            if x not in self.rules:
                rejected_letters.append(x)
        return rejected_letters

    def translate(self, text):
        reformatted_text = text.lower()
        ans_list = []
        for text in reformatted_text:
            for x in self.rules:
                if x == text:
                    ans_list.append(self.rules[x])

        self.ans = ' '.join(ans_list)

        return self.ans
