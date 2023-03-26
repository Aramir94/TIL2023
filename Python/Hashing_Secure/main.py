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