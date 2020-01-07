import requests
import sys

def main():
    print("\n#######################")
    print("#  IP ADDRESS LOOKUP  #")
    print("#######################\n")

    print("1.  My IPv4 Address")
    print("2.  Specify an IPv4 Address")
    print("3.  My IPv6 Address")
    print("4.  Specify an IPv6 Address")
    print("5.  Exit")

    choice = input("\nChoose a number from the menu: ")

    if choice == "1":
        url = "https://ip.nf/me.json"
    elif choice == "2":
        ipAddress = input("\nEnter an IPv4 Address: ")
        url = "https://ip.nf/" + ipAddress + ".json"
    elif choice == "3":
        url = "http://ipv6.ip.nf/me.json"
    elif choice == "4":
        ipv6Address = input("\nEnter an IPv6 Address: ")
        url = "https://ip.nf/" + ipv6Address + ".json"
    elif choice == "5":
        print("\nExiting...\n")
        sys.exit()
    else:
        print("\nInvalid response.  Exiting...\n")
        sys.exit()

    try:
        j = requests.get(url).json()

        print("\nIP ADDRESS   : " + j['ip']['ip'])
        print("AS NUMBER    : " + j['ip']['asn'])
        print("NETMASK      : " + str(j['ip']['netmask']))
        print("CITY         : " + j['ip']['city'])
        print("POSTAL CODE  : " + j['ip']['post_code'])
        print("COUNTRY      : " + j['ip']['country'])
        print("COUNTRY CODE : " + j['ip']['country_code'])
        print("LATITUDE     : " + str(j['ip']['latitude']))
        print("LONGITUDE    : " + str(j['ip']['longitude']) + "\n")

    except Exception:
        print("\nNo information found for that IP address.\n")

if __name__ == "__main__":
    main()
