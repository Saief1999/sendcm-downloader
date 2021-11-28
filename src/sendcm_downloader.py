import requests
import sys
import os
from bs4 import BeautifulSoup

from file_downloader import FileDownloader
class SendcmDownloader:
    """Downloads Send.cm Folders
    """
    def __init__(self, folder_link:str, dest_folder:str=os.path.dirname(__file__)) -> None:
        """ 
        Args:
            folder_link (str): The send.cm folder link
            dest_folder (str): The local destination folder
        """
        self.session = requests.Session()
        self.folder_link = folder_link
        self.file_downloader = FileDownloader(dest_folder)

    def get_folder_content(self):
        """Gets all the files in a Folder
        """
        url = self.folder_link
        base="https://send.cm"
        done = False
        while not done:
            response = self.session.get(url)
            if response.status_code != 200:
                print("Error Loading Page!")
                sys.exit(0)
            soup  = BeautifulSoup(response.content, "html.parser")

            table = soup.find("table", id="xfiles")
            files = table.find_all("a", class_="tx-dark") # these are files
            for file in files:
                self.download_file(file["href"], file.string)
            pagination = soup.find("ul",class_="pagination")
            if pagination == None:
                done = True
            else :
                current_page = pagination.find("li", "page-item actived", recursive=False)
                next_page = current_page.next_sibling # if there is pagination
                if next_page == None:
                    done = True
                else:
                    url = base + next_page["href"]
            
    def get_file_link(self, url:str)->str:
        """Gets the download link for a file

        Args:
            url (str): the file url
        Returns:
            str: its download link
        """
        response = self.session.get(url)
        if response.status_code != 200:
            print("Error Loading Page!")
            sys.exit(0)
        soup = BeautifulSoup(response.content, "html.parser")
        video = soup.find("video") 

        if video == None: # it is not a video
            return None

        return soup.find("video").source["src"]

              

    def download_file(self, url:str, file_name:str):
        """Downloads a file

        Args:
            url (str): file url
            file_name (str): the file name & its extension
        """
        print(f"{file_name}:{url}")
        download_link = self.get_file_link(url)
        direct = False
        form_encoded = None
        if download_link == None: #file isn't a video, download it via api
            form_encoded = {
                "op":"download2",
                "id": url.rsplit("/")[-1],
                "referer": self.folder_link
                }
            download_link = "https://send.cm/"
            direct = True


        self.file_downloader.download(download_link, file_name, form_encoded, direct)





if __name__ == "__main__":
    args = sys.argv[1:] 
    dest_folder = os.path.dirname(__file__)
    if len(args == 0):
        print("Folder Link is required!")
        sys.exit(0)

    folder_link = args[0]    
    if (len(args) >= 2):
        dest_folder = args[1]

    downloader = SendcmDownloader(folder_link, dest_folder)
    downloader.get_folder_content()
    