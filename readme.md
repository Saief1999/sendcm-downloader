# Sendcm Folder Downloader 

<a href="https://colab.research.google.com/github/Saief1999/sendcm-downloader/blob/main/Colab.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

A small tool that gives you the ability to download whole folders from send.cm

![demo](./resources/demo.gif)



## Prerequisites

Make sure you have installed all of the following prerequisites on your machine:
- Python 
- Python packages :
  - Requests : `pip install requests`
  - Beautiful Soup :  `pip install bs4`
  - Clint : `pip install clint`
  - Lxml Parser: `pip install lxml`

## Usage

```
python sendcm_downloader.py [folder_link] [local_path] {--noprogress}
```

- `folder_link`: The Folder URL 
- `local_path` [Optional] : the folder you want to save your files in, defaults to the current folder
- `--noprogress` [Optional] : If, for some reason, you don't want to show the progress of downloading the files
