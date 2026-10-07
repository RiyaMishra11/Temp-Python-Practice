# 116 Context Variables and Context Management
from contextvars import ContextVar, copy_context
from contextlib import contextmanager

# 1 Default value
user = ContextVar("user", default="guest")
print("1.", user.get())

# 2 Set context value
token = user.set("Aman")
print("2.", user.get())

# 3 Reset context value
user.reset(token)
print("3.", user.get())

# 4 Function using ContextVar
request_id = ContextVar("request_id", default="none")

def current_request():
    return request_id.get()

request_id.set("REQ-101")
print("4.", current_request())

# 5 Temporary context value
token = request_id.set("REQ-202")
print("5.", request_id.get())
request_id.reset(token)

# 6 Context manager
@contextmanager
def temporary_user(name):
    token = user.set(name)
    try:
        yield
    finally:
        user.reset(token)

with temporary_user("Riya"):
    print("6.", user.get())
print("   Outside:", user.get())

# 7 Multiple context variables
role = ContextVar("role", default="viewer")
user.set("Rahul")
role.set("admin")
print("7.", user.get(), role.get())

# 8 Copy current context
user.set("Neha")
context = copy_context()
print("8.", context.run(user.get))

# 9 Context-aware message
def context_message(message):
    return f"[user={user.get()}] {message}"

print("9.", context_message("Task started"))

# 10 Request data
request_id.set("REQ-500")
print("10.", {"request_id": request_id.get(), "user": user.get()})

# 11 Nested request context
@contextmanager
def request_context(req_id, username):
    request_token = request_id.set(req_id)
    user_token = user.set(username)
    try:
        yield {"request_id": request_id.get(), "user": user.get()}
    finally:
        request_id.reset(request_token)
        user.reset(user_token)

with request_context("REQ-999", "Admin") as context:
    print("11.", context)
