from pyfiglet import Figlet
import sys

def main():
    figlet = Figlet()
    try:
        if len(sys.argv) == 1:
            s = input("Input: ")
            print(figlet.renderText(s))
        elif len(sys.argv) == 3:
            if sys.argv[1] == "-f":
                figlet.setFont(font= sys.argv[2])
                s = input("Input: ")
                print(figlet.renderText(s))
            else:
                sys.exit("Invalid Usage")
        else:
            sys.exit("Invalid Usage")
    except:
        sys.exit("Invalid Usage")
main()