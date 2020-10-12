import webbrowser
def main():
    website = input("Paste in the URL of the site you want to visit.")
    webbrowser.open(website, new=2)
def nezuko():
    webbrowser.open('https://divine-bird-8888.bss.design/bamboo.html', new=2)
main()
again = int(input("Would you like to do this again? Press 1 for yes, and then anything else for no."))
if again == 1:
    main()
    nezuko()
else:
    print("Goodbye.")
    nezuko()
