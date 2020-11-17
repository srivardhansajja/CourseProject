import subprocess

def webcrawl(primary_url):

    domain = primary_url
    starter = "https://" + domain

    time_limit = 100
    match_limit = 20

    py_ver = 'python3.8'


    py_command = py_ver + " crawler/crawler.py " + domain + " " + starter + " " + str(time_limit) + " " + str(match_limit)

    process = subprocess.Popen(py_command, shell=True)
    process.wait()

    urls = []
    with open('crawler/matched_urls.txt', 'r') as f:
        for line in f:
            urls.append(line)

    return urls
