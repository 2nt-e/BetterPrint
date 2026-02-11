import time

class better:
    def print(content:  str, sepr: str= " ", end: str= "\n"):
        content = str(content)
        c_word = 1
        for words in content.split(" "):        
            if c_word < len(content.split(" ")):
                print(words, end=" ", flush=True)
                time.sleep(0.05)
                c_word += 1
            elif c_word == len(content.split(" ")):
                print(words, end=end, flush=True)
                time.sleep(0.05)


    def input(prompt):
        better.print(prompt, end="")
        return input()
