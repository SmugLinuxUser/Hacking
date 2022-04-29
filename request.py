import requests

filehandler = open("/csxx.txt", "rt")
ass = []
for line in filehandler:
    payload = {'search': '<' + line + '>'}
    r = requests.get('sitegoeshere', params=payload)
    print(r.status_code)
    if r.status_code == 200:
        ass.append(line)


print(ass)
