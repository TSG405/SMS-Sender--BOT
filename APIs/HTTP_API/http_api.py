import requests
from credentials import USERNAME,PWD

print("\n\n---**--- WELCOME TO THE SMS-SENDING BOT ---**---\n")

print("\nAccessing URL...")

# API-URL
url = "https://http-api.d7networks.com/send"

# Driver Code..
def main():
    receiver = input("\nBOT: Type your receiver's PHONE--NUMBER [with the country-code] e.g -:- +919xxxxxxxxx (IND): \t")
    
    try:
        temp=int(receiver)
    except:
        print("BOT: ERROR! Follow the instructions.. and Type correctly !")
        main()
        
    body = input("BOT: Enter the text message: \t")

    querystring = {

    "username":USERNAME,
    "password":PWD,
    "from":"TSG405",
    "content":body,
    "dlr-method":"POST",
    "dlr-url":"https://4ba60af1.ngrok.io/receive",
    "dlr":"yes",
    "dlr-level":"3",
    "to":receiver
  
    }

    headers = {
  
    'cache-control': "no-cache"
  
    }
  
    print("\nBOT: Please wait..\n")
    response = requests.request("GET", url, headers=headers, params=querystring)
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
