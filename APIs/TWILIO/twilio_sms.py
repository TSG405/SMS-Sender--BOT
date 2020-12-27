from twilio.rest import Client
from credentials import SID,TOKEN,sender

print("\n\n---**--- WELCOME TO THE SMS-SENDING BOT ---**---\n")

print("\nAccessing URL...")

# Authroization
client = Client(SID,TOKEN)

# Driver Code..
def main():
    receiver = input("\nBOT: Type your receiver's PHONE--NUMBER [with the country-code] e.g -:- +919xxxxxxxxx (IND): \t")
    
    try:
        temp=int(receiver)
    except:
        print("BOT: ERROR! Follow the instructions.. and Type correctly !")
        main()
        
    bo = input("BOT: Enter the text message: \t")

    print("\nBOT: Please wait..\n")
    
    message = client.messages.create(
    to=receiver, 
    from_=sender,
    body=bo)

    print(message.sid)
    user = input("\nBOT: Want to try again?? Y/N :\t").lower()
    if (user=='y' or user=='yes'):
        print("------------------------------------------------")
        main()
    elif(user=='n' or user=='no'):
       print("\nThank You! \n~TSG405")

main() 



@ CODED BY TSG405, 2020
