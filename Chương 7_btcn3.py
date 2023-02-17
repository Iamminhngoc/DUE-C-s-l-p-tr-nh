s=input('')
def kt(s):
    hoa=False
    thuong=False
    so=False
    kitu=False
    for i in s:
        if i>='A' and i<='Z':
            hoa=True
        if i>='a' and i<='z':
            thuong=True
        if i>='0' and i<='9':
            so=True
        if i in '$#@':
            kitu=True
    if len(s)>=6 and len(s)<=17 and hoa and thuong and so and kitu:
        return True
    return False
print(kt(s))  