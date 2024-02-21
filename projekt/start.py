import subprocess

def leta_ip():
    print("Starting leta-ip.py...")
    subprocess.run(["python3", "./leta-ip.py"])

def sth_hash_find():
    hash_text = input("Ange hash att försöka lösa: ")
    subprocess.run(["python3", "/usr/local/bin/sth", "-t", hash_text])

def main():
    while True:
        print("\nMenu:")
        print("[1] Sök upp en IPv4 adress")
        print("[2] Försök lösa en hash MD5/SHA")
        print("[X] Avsluta")

        choice = input("Ange ditt val: ")

        if choice == '1':
            leta_ip()
        elif choice == '2':
            sth_hash_find()
        elif choice.lower() == 'x':
            print("Avslutar. Hejdå!")
            break
        else:
            print("Felaktigt val. försök igen!")

if __name__ == "__main__":
    main()
