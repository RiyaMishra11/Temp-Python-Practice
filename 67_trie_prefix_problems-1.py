"""Day 16 - File 67: Trie and Prefix Problems | 11 Programs"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children: return False
            node = node.children[ch]
        return node.is_end
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children: return False
            node = node.children[ch]
        return True

def program_1():
    t=Trie()
    for w in ["cat","car","cart","dog"]: t.insert(w)
    print("Inserted successfully")

def program_2():
    t=Trie()
    for w in ["apple","app","apply"]: t.insert(w)
    print(t.search("apple"), t.search("ape"))

def program_3():
    t=Trie()
    for w in ["apple","application","apply"]: t.insert(w)
    print(t.starts_with("app"), t.starts_with("xyz"))

def program_4():
    words=["car","card","care","cat","dog"]
    print(sum(w.startswith("car") for w in words))

def program_5():
    words=["apple","app","application","banana","apply"]
    print([w for w in words if w.startswith("app")])

def program_6():
    words=["flower","flow","flight"]
    prefix=words[0]
    for w in words[1:]:
        while not w.startswith(prefix): prefix=prefix[:-1]
    print("Longest common prefix:", prefix)

def program_7():
    words=["apple","app","ape","banana"]
    freq={}
    for w in words:
        for i in range(1,len(w)+1):
            freq[w[:i]]=freq.get(w[:i],0)+1
    print(freq)

def program_8():
    words=["python","pytorch","pyramid","java","javascript"]
    print([w for w in words if w.startswith("py")])

def program_9():
    words=["zebra","dog","duck","dove"]
    for w in words:
        for i in range(1,len(w)+1):
            p=w[:i]
            if sum(x.startswith(p) for x in words)==1:
                print(w,"->",p); break

def program_10():
    t=Trie()
    for w in ["hello","world","python","programming"]: t.insert(w)
    for q in ["python","java","hello"]: print(q, t.search(q))

def program_11():
    words=["python","pandas","programming","project","pytest","javascript"]
    print("Autocomplete:", sorted(w for w in words if w.startswith("pro")))

if __name__ == "__main__":
    program_1()
