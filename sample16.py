APPROVED = ["Canvas", "Teams", "Scratch"]
RESTRICTED = ["TikTok", "Fortnite"]

READ = 1     
WRITE = 2   
EXECUTE = 4  

def check_access(name, app, user_perms):
    if type(name) != str or type(app) != str or type(user_perms) != int:
        print("Error: Wrong data type entered!")
        return

    if app in RESTRICTED or app not in APPROVED:
        print(f"Access Denied: {app} is not allowed.")
        return

    needed_perms = READ | EXECUTE 
    
    if (user_perms & needed_perms) != needed_perms:
        print("Access Denied: You don't have the right permissions.")
        return

    print(f"Access Granted to {name} for {app}!")
    print(f"Shift Left (Double value): {user_perms << 1}")
    print(f"Shift Right (Halve value): {user_perms >> 1}")

check_access("Alex", "Canvas", 5)