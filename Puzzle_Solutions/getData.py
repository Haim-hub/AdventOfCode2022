#
import requests


def getInput(day):
    url = f'https://adventofcode.com/2022/day/{day}/input'
    cookie = '53616c7465645f5f1722984b2ed210b845a23237eb9e94a3a553dcb35f302042bd7fc0656ec7babbb2d9eb3bf1a163611549cb9fe69065ec6adf338852ea07b0'
    s = requests.Session()

    data = s.get(url, cookies={'session': cookie})
    return (data.text)
