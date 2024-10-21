import base64

a="pbkdf2:sha256:600000$YnRgjnim$c9541a8c6ad40bc064979bc446025041ffac9af2f762726971d8a28272c550ed"

heist=a.replace("$",":").split(":")

heist[-2] = base64.b64encode(heist[-2].encode()).decode()

heist[-1]=base64.b64encode(bytes.fromhex(heist[-1])).decode()

print(":".join(heist))
