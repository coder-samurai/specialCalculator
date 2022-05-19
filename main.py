# modules
import os, sys

# install modules Colorama
try:
    from colorama import Fore, Back
except:
    try:
        os.system("python3 install colorama")
    except:
        os.system("python install colorama")



# calculator
class App:

    def __init__(self):
        pass

    def logo(self):
        # logo
        logo = f""" {Fore.CYAN}
█▀ ▄▀█ █▀▄▀█ █░█ █▀█ ▄▀█ █
▄█ █▀█ █░▀░█ █▄█ █▀▄ █▀█ █ IG: samuraicoder
        """

        return logo

    def Run(self):
        # show logo
        print(self.logo())

        # how many times
        times = input(f"\n\n{Fore.BLUE}How many times:  {Fore.WHITE}")
        times = int(times)

        # list for to save results
        List = []

        for i in range(times):
            answer = input(f"\n{Fore.MAGENTA}Calculator:  {Fore.WHITE}")
            if "x" in answer:
                answer = answer.replace("x", "*")
            output = eval(answer)
            List.append(output)
            print(f"\n{Fore.RED}output: {Fore.WHITE}{output}")

        # show total
        total = sum(List)
        print(f"\n\n{Fore.RED}Total: {Fore.RESET}{total}")

        # again?
        again = input(f"\n\nAgain (y/n):  ")
        again = again.upper()
        
        if again == "Y":
            self.cleanTerminal()
            os.execv(sys.executable, ['python'] + sys.argv)
            exit()
        else:
            self.cleanTerminal()

        
    def cleanTerminal(self):
        # clean terminal
        try:
            os.system("clear")
        except:
            os.system("cls")

# run script
if __name__ == "__main__":
    App = App()
    App.Run()