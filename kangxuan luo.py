def errorcode(x):
    match x:
        case 500:
            return"Internal Server Error"
        case 401:
            return"Unauthorised "
        case 400:
            return"Bad Request "
        case 403:
            return"Forbidden "
        case 404:
            return"Not Found "

x = int(input("the error code is:"))
print(errorcode(x))
