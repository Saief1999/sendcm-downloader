import requests
from clint.textui import progress

class FileDownloader:
    """
    Download a File from a link
    """

    def __init__(self, dest_folder, noprogress=False) -> None:
        self.session = requests.Session()
        self.dest_folder = dest_folder
        self.noprogress= noprogress


    def download_request(self, url, form_encoded):
        if form_encoded != None:
            redirected_response = self.session.post(url, data=form_encoded,
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                allow_redirects=False)
            return redirected_response.headers["Location"]
        return url

    def download(self, url:str, name:str="file", form_encoded=None):
        """
        Downloads a file
        """
            
        response = self.session.get(self.download_request(url, form_encoded=form_encoded), stream=not self.noprogress)
        filepath=f"{self.dest_folder}/{name}"
        if response.status_code == 200:
            if self.noprogress:
                with open(filepath, 'wb') as f:
                    f.write(response.content)

            else : 
                total_length=int(response.headers.get('content-length'))        
   
                with open(filepath, 'wb') as f:
                    for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                        if chunk:
                            f.write(chunk)   
                            f.flush()