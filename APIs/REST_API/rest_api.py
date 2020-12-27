import requests
from credentials import AUTH

print("\n\n---**--- WELCOME TO THE SMS-SENDING BOT ---**---\n")

print("\nAccessing URL...")

# API-URL
url = "https://rest-api.d7networks.com/secure/send"

# Driver Code..
def main():
    receiver = input("\nBOT: Type your receiver's PHONE--NUMBER [with the country-code] e.g -:- +919xxxxxxxxx (IND): \t")
    
    try:
        temp=int(receiver)
    except:
        print("BOT: ERROR! Follow the instructions.. and Type correctly !")
        main()
        
    R = '\"'+receiver+'\"'
    
    body = input("BOT: Enter the text message: \t")
    B = '\"'+body+'\"'
    
    payload = "{\n\t\"to\":"+R+",\n\t\"content\":"+B+",\n\t\"from\":\"TSG405\",\n\t\"dlr\":\"yes\",\n\t\"dlr-method\":\"GET\", \n\t\"dlr-level\":\"2\", \n\t\"dlr-url\":\"http://yourcustompostbackurl.com\"\n}"

    headers = {
    
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': AUTH
  
    }
  
    print("\nBOT: Please wait..\n")
    response = requests.request("POST", url, headers=headers, data = payload)
    if ('Success' in response.text):
        print("BOT: **!MESSAGE SENT SUCCESSFULLY!**")
    else:
        print("BOT: ERROR!! Please Try again Later!")
    user = input("\nBOT: Want to try again?? Y/N :\t").lower()
    if (user=='y' or user=='yes'):
        print("------------------------------------------------")
        main()
    elif(user=='n' or user=='no'):
       print("\nThank You! \n~TSG405")

main() 



@ CODED BY TSG405, 2020
