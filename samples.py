def download_list_of_files():

    url_list = None

    with open('url_list.txt') as f:
        url_list = [line for line in f]

    for url in url_list:

        url = url.replace('\n','')

        res = requests.get(url, stream=True)
        with open("output/"+url.split('/')[-1], "wb") as f:
            f.write(res.content)