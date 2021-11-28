import requests
from clint.textui import progress
import os

class FileDownloader:

    def __init__(self, dest_folder= os.path.dirname(__file__)) -> None:
        self.session = requests.Session()
        self.dest_folder = dest_folder


    def download_request(self, url, form_encoded, direct=False):
        if not direct:
            response = self.session.get(url, stream=True)
        else:
            redirected_response = self.session.post(url, data=form_encoded,
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                allow_redirects=False)
            
            response = self.session.get(redirected_response.headers["Location"], stream=True)
        return response

    def download(self, url:str, name:str="file", form_encoded=None, direct=False):
        """
        Downloads a file
        """
        response = self.download_request(url, form_encoded=form_encoded, direct=direct)
        filepath=f"{self.dest_folder}/{name}"
        if response.status_code == 200:
            total_length=int(response.headers.get('content-length'))
            with open(filepath, 'wb') as f:
                for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                    if chunk:
                        f.write(chunk)   

if __name__ == "__main__":
    downloader = FileDownloader()
    downloader.download("https://eu1rgn-down.file.samsungcloud.com/file/v2/blobs/e0855ec04eca11ecb9cc3253757ab7ed/signed?signature=F48oUezgweoeU5wlo-zvQ0SyOzJq55rB1M9WIq5fwkMbLJils14owK3sMqsxmx8Icoi0-qb5hEiFf9Srfv1cH1AjFlF_PL_je-Pw_quXgjwIa93BMt4MLzby_5uO7rYJbc4LVopup-kZ48KWGpEYQkFVm9PcHzNfSwGkKV4caWT8OW07lNB0EK6L8bPDRc08fs2woHm-UUOq3s61BPbFsUdecTty-sgQpI_RI52ruaCt7YOeFZJj64LUwxe7Hw8r-DL3a83cnVae3IzkkQakZBnwKk2sHB94n2A88n4wafg&v=3206762&cid=A411ZXFWwq&name=Forum_211126_160722.txt","forum")