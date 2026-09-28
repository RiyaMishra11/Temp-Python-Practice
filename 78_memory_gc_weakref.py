# Python Practice 78: Memory, Garbage Collection & Weak References
import gc
import weakref
from dataclasses import dataclass

# 1. Object identity
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("1.", id(a) == id(b), id(a) == id(c))

# 2. References
class Demo: pass
obj = Demo()
ref = obj
print("2.", ref is obj)
del ref
print("   Original object:", obj is not None)

# 3. Circular reference
class Node:
    def __init__(self, name):
        self.name = name
        self.link = None

x, y = Node("X"), Node("Y")
x.link, y.link = y, x
del x, y
print("3. Circular references created and released")

# 4. Manual garbage collection
print("4. Collected:", gc.collect())

# 5. GC state
old = gc.isenabled()
gc.disable()
print("5. GC enabled:", gc.isenabled())
if old:
    gc.enable()

# 6. Tracked objects
print("6. Tracked objects:", len(gc.get_objects()))

# 7. Weak reference
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"User({self.name!r})"

user = User("Aman")
w = weakref.ref(user)
print("7. Before:", w())
del user
print("   After:", w())

# 8. WeakKeyDictionary
class Item: pass
item1, item2 = Item(), Item()
notes = weakref.WeakKeyDictionary({item1: "first", item2: "second"})
print("8. Size:", len(notes))
del item1
gc.collect()
print("   After deletion:", len(notes))

# 9. WeakSet
class Session: pass
s1, s2 = Session(), Session()
active = weakref.WeakSet([s1, s2])
print("9. Sessions:", len(active))
del s1
gc.collect()
print("   After deletion:", len(active))

# 10. Destructor demonstration
class Resource:
    def __del__(self):
        print("10. Resource cleanup called")

r = Resource()
del r
gc.collect()

# 11. Weak-value cache
@dataclass
class Product:
    name: str

cache = weakref.WeakValueDictionary()
p = Product("Laptop")
cache["p1"] = p
print("11. Cached:", cache.get("p1"))
del p
gc.collect()
print("   After deletion:", cache.get("p1"))
