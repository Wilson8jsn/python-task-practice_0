import zipfile


def extract_file(zfile, password):
    try:
        zfile.extractall(pwd=password.encode('utf-8'))
        return password
    except Exception as error:
        print(f"Bad password for file: {error}")
        return None

def main():
    zfile = zipfile.ZipFile("name.zip")
    pass_file = open('dictionary.txt')
    
    for line in pass_file.readlines():
        password = line.strip("\n")
        guess = extract_file(zfile=zfile, password=password)
        
        if guess:
            print(f"[+] Password found: {password}")
            exit(0)
    
    print("Password not found in dictionary.")
    
if __name__ == '__main__':
    main()
