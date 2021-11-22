from os.path import join
import requests


def img_url_2_data(url):
    return url.split('?')[0].split('/')[-1].split('.')


def save_file_from_url(url, savepath, name=None):
    response = requests.get(url)

    data = img_url_2_data(url)
    if name is None:
        name = data[0]
    img_format = data[1]

    with open(join(savepath, name + '.' + img_format), 'wb') as file:
        file.write(response.content)
