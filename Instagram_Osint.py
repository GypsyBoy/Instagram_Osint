import requests
import sys
from colorama import Fore,init
init()

def print_baner():
    print(Fore.GREEN+"""
 _______________________________________
|	   Profile Downloader	        |
|	   Author: Gypsyboy	        |
|	   Tel: @Xor_021		|
|	   Channel: @ArgentCrusaders0	|
|	   Github:github.com/gypsyboy	|
|_______________________________________|  
                        """)

def download_profile(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(Fore.GREEN+"[+] Downloading image...")
            image_response = requests.get(url)
            with open("profile_picture.jpg", "wb") as file:
                file.write(image_response.content)
            print(Fore.GREEN+"[+] Image downloaded successfully!")
        else:
            print(Fore.RED+"[-] Invalid URL or permissions issue.")
    except Exception as e:
        print(Fore.RED+"[!] Error:", e)

def get_user_by_user_id(user_id):
    user = {}
    if user_id:
        base_url = "https://i.instagram.com/api/v1/users/{}/info/"
        #valid user-agent
        headers = {
            'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
        }
        try:
            res       = requests.get(base_url.format(user_id),headers=headers)
            user_info = res.json()
            user      = user_info.get('user',{})
        except Exception as e:
            print("getting user failed, due to '{}'".format(e.message))
    return user



def main():
    print_baner()
    print(Fore.RED+"[!] Note : Always run this script with VPN! \n")
    print(Fore.GREEN+"""Chose an option:
    [1]  Download
    [2]  ID-to-Username 
    [99] Exit
    """)
    chosen_option = int(input("#> "))
    
    if chosen_option == 1:
        url = input("Please enter url : ")
        download_profile(url=url)
    elif chosen_option == 2:
        user_id = int(input("Please enter id : "))
        res = get_user_by_user_id(user_id)
        print(res)
    elif chosen_option == 99:
        sys.exit("Exiting...")
    else:
        print(Fore.RED+"[!] Invalid input! \n exiting...")
        sys.exit(2)


main()




