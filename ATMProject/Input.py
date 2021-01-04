class Validator:
    def getInteger(self, prompt, min, max):
        while True:
            try:
                inputString = input(prompt)
                inputInt = int(inputString)

                if (inputInt >= min) and (inputInt <= max):
                    return inputInt
            except:
                continue

    def getFloat(self, prompt, min, max):
        while True:
            try:
                inputString = input(prompt)
                inputFloat = float(inputString)

                if (inputFloat >= min) and (inputFloat <= max):
                    return inputFloat
            except:
                continue
