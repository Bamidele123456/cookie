import uuid




email= "bamideleprecious85@gmail.com"
email2 = "bamidleprecious@gmail.com"

user_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, email))
user_id2 = str(uuid.uuid5(uuid.NAMESPACE_DNS, email2))

print(user_id)
print(user_id2)