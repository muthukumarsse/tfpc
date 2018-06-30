import requests

def check_url(extension):
    url = "http://tamilrockers.%s" % (extension,)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            if "Watch Latest Tamil" in r.text:
                return True
    except:
        pass
    return False

def main():
    a = range(97,123)
    b = a
    possible_extensions = []
    for i in a:
        for j in b:
            possible_extensions.append(
                "%s%s" % (chr(i), chr(j))
            )
    working = []
    not_working = []
    for extension in possible_extensions:
        if check_url(extension):
            working.append(extension)
        else:
            not_working.append(extension)
    print "Working: ", working
    print "Not Working: ", not_working

if __name__ == '__main__':
    main()
