from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(similar("Where are you?", "I haven't heard of you in a few days, where are you"))
print(similar("Where are you?", "Hello, you mom seys thet where are you"))
