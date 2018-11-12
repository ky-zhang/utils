import requests
from bs4 import BeautifulSoup

def download_file(url, index, folder):
    download_dir = './' + folder + '/' + '{:02}'.format(index) + url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(download_dir, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return download_dir

def download_page(folder):
    # root_link is the root url of files
    root_link = 'https://utdallas.edu/~kyle.fox/courses/cs6301.008.18s/lectures/'
    r = requests.get(root_link)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html5lib")
        index = 0
        print("\n=============== Start Downloading ===============\n")
        for link in soup.find_all('a'):
            new_link = root_link + link.get('href')
            print(new_link)
            if new_link.endswith('.pdf') or new_link.endswith('.zip'):
                download_dir = download_file(new_link, index, folder)
                print("Dowloading: {} ==>  {}".format(new_link.split('/')[-1], download_dir))
                index += 1
        print("\n=============== Download Finished ===============\n")
        print('Totally %d files have been downloaded.'%(index))
    else:
        print("Error!")

if __name__ == '__main__':
    # the directory you want to save the downloaded files
    # make sure you have create it before download
    download_page("lectures")