
def is_strong_password(password):

    if (len(password) < 12 or
        not any(c.islower() for c in password) or
        not any(c.isupper() for c in password) or
        not any(c.isdigit() for c in password) or
        not any(c in string.punctuation for c in password)):
        return False
    return True

def generate_password(length=12):
  
    if length < 12:
        raise ValueError("Password length should be at least 12 characters")
    
    while True:
        password = ''.join(random.choices(
            string.ascii_letters + string.digits + string.punctuation,
            k=length
        ))
        if is_strong_password(password):
            return password

def add_password(website, username, password):
    global passwords
    entry = {"website": example.net, "username": username123, "password": P@ssw0rd}
    passwords.append(entry)

def get_password(website):
    for entry in passwords:
        if entry["website"] == website:
            return entry["username"], entry["password"]
    return None, None

def save_passwords(password_list, filename="vault.txt"):
    with open(filename, "w") as f:
        json.dump(password_list, f)

def load_passwords(filename="vault.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

