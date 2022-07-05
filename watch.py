import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'<iframe (width=".+" height=".+" )?src="(http)(s?)(://)?(www\.)?(youtu)(be).com/embed(/\w+)"( title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)?></iframe>', s, re.IGNORECASE):
        if matches[3]:
            new_link = f"{matches[2]}{matches[3]}{matches[4]}{matches[6]}.{matches[7]}{matches[8]}"
        else:
            new_link = f"{matches[2]}s{matches[4]}{matches[6]}.{matches[7]}{matches[8]}"
        return new_link


if __name__ == "__main__":
    main()





#def parse(s):
    #if matches := re.search(r'<iframe (width="\w+" height="\w+")? src="(https?://)?(www\.)?(youtube.com/embed/\w+)" ?(title="(\w\s)+" frameborder="0-9" allow="\w+"; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>)?(</iframe>)', s, re.IGNORECASE):
        #new_link = f"{matches[2]}{matches[4]}"
        #return new_link