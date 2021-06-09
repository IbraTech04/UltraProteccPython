import urllib.request
import datetime
import traceback

today = datetime.datetime.now()


print("UltraProtecc Key Validator")
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
        day = splitKey[0][:3]
        year = splitKey[0][3:]
        yearActual = today.year
        if ("20" + year == str(today.year)):
            day_of_year = today.timetuple().tm_yday  
            if (day_of_year - int(day) < 30):
                print("Key is Valid")
                print("key has ", int(day) + 30 - day_of_year , "Days left")
            else:
                print("key is expired")

        else:
            print("key is expired")

    elif splitKey[1] == "RTL":
        print("key is retail key")
        print("most likely accuired from a vendor")

except:
    print("invalid key intered")
    traceback.print_exc()

