import requests

def main():
    w = input('Enter website to check the status off.')
    if not w.startswith("https://") or w.startswith("http://"):
        print("Please include http/https.")
        main()
    try:
        ww = requests.get(w)
    except Exception as e:
        print(e)
        print('\nWebsite is down or your request was blocked.')
        exit()
    #Add more status codes if you want, these are just the codes I thought off.
    if ww.status_code == 404:
        x = "Page could not be found, 404."
    elif ww.status_code == 200:
        x = "Page was found, 200."
    elif ww.status_code == 503:
        x = "Service unavailbale, 503."
    else:
        x = ww.status_code
    print("Result:",x)

    #Logging section.
    f = open('logs.txt', 'a')
    f.write(w+":"+" "+str(ww.status_code))
    f.close()

main()
