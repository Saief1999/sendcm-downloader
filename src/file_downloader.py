import requests
from clint.textui import progress
import os

class FileDownloader:
    """
    Download a File from a link
    """

    def __init__(self, dest_folder) -> None:
        self.session = requests.Session()
        self.dest_folder = dest_folder


    def download_request(self, url, form_encoded):
        if form_encoded != None:
            redirected_response = self.session.post(url, data=form_encoded,
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                allow_redirects=False)
                
            return self.session.get(redirected_response.headers["Location"], stream=True)

        return self.session.get(url, stream=True)

    def download(self, url:str, name:str="file", form_encoded=None):
        """
        Downloads a file
        """
        response = self.download_request(url, form_encoded=form_encoded)
        filepath=f"{self.dest_folder}/{name}"
        if response.status_code == 200:
            total_length=int(response.headers.get('content-length'))
            with open(filepath, 'wb') as f:
                for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                    if chunk:
                        f.write(chunk)   