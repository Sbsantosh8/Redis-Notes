import redis


r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# Create a user profile (Hash)
r.hset(
    "user:1001",
    mapping={"name": "Santosh", "email": "santosh@example.com", "age": "24"},
)

# Get one field
print(r.hget("user:1001", "email"))  # santosh@example.com

# Get all fields
print(r.hgetall("user:1001"))
# {'name': 'Santosh', 'email': 'santosh@example.com', 'age': '24'}

# Update one field
r.hset("user:1001", "age", "25")

# Increment numeric field
r.hincrby("user:1001", "age", 1)
print(r.hget("user:1001", "age"))  # 26
