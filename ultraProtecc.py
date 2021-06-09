import urllib.request

print("TMUltraProtecc Key Validator")
keyToCheck = input("Please enter the key you would like to validate: ")
productOwner = input("Please enter the username attached to this key: ")

splitKey = keyToCheck.split("-")

try:
    ##Getting total ASCII value of the username
    totalAsciiVal = 0
    for x in productOwner:
        totalAsciiVal += ord(x)
    ##If the key is OEM:
    if splitKey[1] == "OEM":
        print("key is OEM key")
        print("most likely preinstalled software")
        stageOne = 0
        for i in range(7): ##Add up all the digits in the third segment
            stageOne += int(splitKey[2][i])
        stageTwo = 0
        for i in range(5): ##Add up all the digits in the fourth segment
            stageTwo += int(splitKey[3][i])
        ##If the total ASCII value is equal to the product key, and the sum of S3 is divisible by 7, and the sum of S4 is divisible by 5
        if (totalAsciiVal == int(splitKey[4]) and stageOne % 7 == 0 and stageTwo % 5 == 0):
            print("key is valid")
            print("checking server for activation of key")
            url = "https://raw.githubusercontent.com/IbraTech04/updateServer/master/activeTMQMKeys.txt"
            filename, headers = urllib.request.urlretrieve(url, filename="./keys.txt")
            f = open("keys.txt", "r")
            final = f.read()
            for i in final:
                if (i in keyToCheck):
                    
                    print("serverside passed")
                    break
        else:
            print("key is not valid")
    elif splitKey[1] == "TRL":
        print("key is trial key")


    elif splitKey[1] == "RTL":
        print("key is retail key")
        print("most likely accuired from a vendor")

except:
    print("invalid key intered")
