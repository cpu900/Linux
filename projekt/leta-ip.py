#!/usr/bin/env python3

import ipapi

### Filer som skrivs/läs från
fil_ip_info = 'ip.txt'

### Hämta in en IP adress
def get_ip():
	return input("Enter target IP address: ")
	

### Letar upp info om IPv4 mha ipapi.co
def get_info(ip_address):
    try:
	# Spara result av sökningen
        result = ipapi.location(ip_address)

	# for k, v in result.items():
        #     print(str(k) + " : " + str(v))

        with open(fil_ip_info, 'w') as file:
            for k, v in result.items():
                file.write(f"{k} : {v}\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")	

### Läs från fil här
def read_file():
    try:
        with open(fil_ip_info, 'r') as file:
            lines = file.readlines()

            # Hämta ut värden att visa från filen
            ip = lines[0].split(':')[1].strip()
            city = lines[3].split(':')[1].strip()
            country = lines[7].split(':')[1].strip()
            org = lines[25].split(':')[1].strip()
            asn = lines[26].split(':')[1].strip()

            # Skriv ut formaterad
            print(f"[*] IP: {ip} | {city}/{country} | {asn}/{org}")

    except Exception as e:
        print(f"Error: {e}")


### Main funktionen
if __name__ == "__main__":

    # Hämta ip att söka på    
    sok_ip = get_ip()
    # Hämta info om IP
    get_info(sok_ip)
    # Läs från fil
    read_file()

