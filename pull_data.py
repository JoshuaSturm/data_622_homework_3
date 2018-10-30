'''
DATA 622 - Homework 2
Joshua Sturm
10/05/2018

This script will retrieve the training and testing data sets from the following respective urls:
- https://www.kaggle.com/c/titanic/download/train.csv
- https://www.kaggle.com/c/titanic/download/test.csv
'''

# Import libraries
import requests

# Remote files
# user = credentials.login['email']
# pw = credentials.login['password']

'''
Note, that you will need to create a fille called 'credentials.py' with the following structure:

login = {
    'email' : '',
    'password' : ''
}
'''

payload = {
    'action':'login',
    'username': iamfleurdelys@gmail.com,
    'password': tempproject
}

loginUrl = "https://www.kaggle.com/account/login"
train_url = 'https://www.kaggle.com/c/titanic/download/train.csv'
test_url = 'https://www.kaggle.com/c/titanic/download/test.csv'
kaggle_files = [train_url, test_url]

# Files that will be saved locally
local_train = 'train.csv'
local_test = 'test.csv'
local_files = [local_train, local_test]

# for file, lfile in zip(kaggle_files, local_files):
#         resp_get = requests.get(file, auth = (user, pw))
#         # resp = requests.get(file, auth = (user, pw))
#         resp_get1 = requests.get(file)
#         resp = requests.post(resp_get1.url, allow_redirects = False)
#         # resp = requests.get(file)
#         print(resp.url)
#
#
#         # f = open(lfile, 'w')
#         #
#         # for chunk in resp.iter_content():
#         #     if chunk:
#         #         f.write(chunk)
#         # f.close()
#
#         # with open(lfile, 'wb') as fd:
#         #     for chunk in resp.iter_content(chunk_size = 512 * 1024):
#         #         fd.write(chunk)
#         with open(lfile, 'wb') as fd:
#             fd.write(resp.content)
#         fd.close()

with requests.session() as c:
        response = c.get(loginUrl).text
        AFToken = response[response.index('antiForgeryToken')+19:response.index('isAnonymous: ')-12]
        payload['__RequestVerificationToken']=AFToken
        c.post(loginUrl + '?IsModal=true&returnUrl=/', data=payload)
        # get request

        for file, lfile in zip(kaggle_files, local_files):
                with open(lfile, 'wb') as handle:  #python3 needs wb, python2 only w
                        response = c.get(file, stream=True)
                #print(response.text)
                        for block in response.iter_content(1024):  #capture the data in k sized chunks
                                handle.write(block)

'''
References:
- https://stackoverflow.com/a/34230732/8877639
- https://www.reddit.com/r/learnpython/comments/264ffw/what_is_the_pythonic_way_of_storing_credentials/
- https://stackoverflow.com/a/43519016/8877639
- https://stackoverflow.com/a/50876207/8877639
- https://github.com/graemerenfrew/titanic/blob/master/notebooks/1.0-ak-extract-titanic-data.ipynb
'''
