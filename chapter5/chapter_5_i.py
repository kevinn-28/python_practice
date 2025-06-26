book ={"gift":"something given to another", "this":"the thing at hand", "that":"the thing over there"
,"youtube":"a video sharing platform", "instagram":"a photo sharing platform",
"example":[1,2,3,4,5]}

book.update({"kevin": "a person","example":[12,24]})
print(book.items())
print(book.keys())
for a , b in book.items():
    print(a, b)
for c in book.keys():
    print(c)
print(book.get("hi"))
