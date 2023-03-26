# incrypted way 
"""
encode and decode them -> receive message and decode message to see 
"""

# hashing way
"""
only encode them -> check send message is right!
"""

import hashlib
print(hashlib.algorithms_available)

h = hashlib.new("SHA256")
h.update(b"Hello World!") 
#print(h.digest())
print(h.hexdigest())

## What about Password to database 
correct_password = "Mypassword1234"
h = hashlib.new("SHA256") # new로 새로 만들어 줘야한다
h.update(correct_password.encode())
password_hash = h.hexdigest()
print(password_hash)

user_input = "Mypassword1234"
h = hashlib.new("SHA256") # new로 새로 만들어 줘야한다
h.update(user_input.encode())
user_password_hash = h.hexdigest()
print(user_password_hash)

print(password_hash ==user_password_hash)