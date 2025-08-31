import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.set("name", "John")
print(r.get("name"))

print(type(r.get("name")))


r.set("user:1001", "Mahesh")
print(r.get("user:1001"))


r.set("pages:view", 0)
r.incr("pages:view")
print(r.get("pages:view"))


user_id = 1003
# r.set(f"user:{user_id}:profile", '{"name": "Sahadev", "age": 24}', ex=10)

print(r.get(f"user:{user_id}:profile"))

# TTL (Time to Live )

print(r.ttl(f"user:{user_id}:profile"))



