import os

envName = os.environ.get('ENV_NAME', 'heroLogin')
browser = os.environ.get('BROWSER', 'chrome')

url = {
    'heroLogin': 'https://the-internet.herokuapp.com',
    'bing': 'https://www.bing.com/',
}

writeLoginUrl = url['heroLogin'] if envName == 'heroLogin' else url['bing']

result = {
    'writeLoginUrl': writeLoginUrl,
    'env': envName,
    'browser': browser
}

