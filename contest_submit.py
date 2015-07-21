import requests
files = {'file': open('a+b.py', 'rb')}
#submit
req1 = requests.post('https://api.contest.yandex.net/anytask/submit', data={'compilerId': 'python3', 'contestId': 1316, 'problemId': '2537/2015_07_07/GoMAw60KFk'}, files=files, headers={'Authorization': 'OAuth 61a1df2df495415b86eb777e771fd057'})
print(req1.text)
#contest_info
req2 = requests.get('https://api.contest.yandex.net/anytask/problems?contestId=1316&locale=ru', headers={'Authorization': 'OAuth 61a1df2df495415b86eb777e771fd057'})
print(req2.text)
#results
req3 = requests.get('https://api.contest.yandex.net/anytask/results?runId=717993&contestId=1316', headers={'Authorization': 'OAuth 61a1df2df495415b86eb777e771fd057'})
print(req3.text)
