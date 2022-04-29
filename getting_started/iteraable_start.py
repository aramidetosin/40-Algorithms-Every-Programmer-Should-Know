words = "Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. " \
        "If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- " \
        "let's do more of those!".split()

words_list = [len(word) for word in words]
words_list.sort()
print(words_list)


import os, glob, pprint

file_size = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob("*.py")}
pprint.pprint(file_size)