import requests
from credentials import USERNAME,PWD

print("\n\n---**--- WELCOME TO THE SMS-SENDING BOT ---**---\n")

print("\nAccessing URL...")

# API-URL
url = "http://smsc.d7networks.com:4545/jasmin/api?wsdl"

# Driver Code..
def main():
    receiver = input("\nBOT: Type your receiver's PHONE--NUMBER [with the country-code] e.g -:- 919xxxxxxxxx (IND): \t")
    
    try:
        temp=int(receiver)
    except:
        print("BOT: ERROR! Follow the instructions.. and Type correctly !")
        main()
        
    body = input("BOT: Enter the text message: \t")

    payload = "<x:Envelope xmlns:x=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:tns=\"tns\">\n   <x:Header/>\n   <x:Body>\n       <tns:send>\n           <tns:username>"+USERNAME+"</tns:username>\n           <tns:password>"+PWD+"</tns:password>\n           <tns:source_addr>TSG405</tns:source_addr>\n           <tns:destination_addr>"+receiver+"</tns:destination_addr>\n           <tns:coding>8</tns:coding>\n           <tns:dlr>yes</tns:dlr>\n           <tns:dlr_url>http://sms.d7networks.com/dlr_receiver</tns:dlr_url>\n           <tns:dlr_level>2</tns:dlr_level>\n           <tns:dlr_method>GET</tns:dlr_method>\n           <tns:content>"+body+"</tns:content>\n       </tns:send>\n   </x:Body>\n</x:Envelope>"

    headers = {}
  
    print("\nBOT: Please wait..\n")
    response = requests.request("POST", url, headers=headers, data = payload)
    if ('Success' in response.text.encode('utf8')):
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
