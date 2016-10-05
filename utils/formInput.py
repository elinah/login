def register(username, password):
    file = open('./data/info', 'a+')
    for line in file:
      if username == line.split(",")[0]:
        file.close()
        return "Username already taken."
    file.write(username + "," + password + "\n")
    file.close()
    return "Successfully registered!"
    
def login(username, password):
    file = open('./data/info', 'a+')
    for line in file:
      l = line.split(",")
      if username == l[0]:
        if password == l[1].rstrip("\n"):
          file.close()
          return "Yay you successfully logged in!"
        else:
          file.close()
          return "Incorrect password."
    file.close()
    return "Username does not exist."