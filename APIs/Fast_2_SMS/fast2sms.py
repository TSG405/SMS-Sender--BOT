import requests
from credentials import AUTH

print("\n\n---**--- WELCOME TO THE SMS-SENDING BOT ---**---\n")

print("\nAccessing URL...")

# API-URL
url = "https://www.fast2sms.com/dev/bulk"

# Driver Code..
def main():
    receiver = input("\nBOT: Type your receiver's PHONE--NUMBER e.g -:- 9xxxxxxxxx (IND): \t")
    
    try:
        temp=int(receiver)
    except:
        print("BOT: ERROR! Follow the instructions.. and Type correctly !")
        main()
        
    body = input("BOT: Enter the text message: \t")

    payload = "sender_id=FSTSMS&message="+body+"&language=english&route=p&numbers="+receiver
   
    headers = {
    
           'authorization': AUTH,
           'Content-Type': "application/x-www-form-urlencoded",
           'Cache-Control': "no-cache",
           
           }
           
    print("\nBOT: Please wait..\n")
    response = requests.request("POST", url, data=payload, headers=headers)
    if 'Message sent successfully to NonDND numbers' in (response.text):
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
