# Sendcm Folder Downloader 

a small tool that gives the ability to download whole folders from send.cm

![demo](./resources/demo.gif)



## Disclaimer 

Support for all kinds of files still needs some testing, feel free to report any bugs you find! 

## Prerequisites

Make sure you have installed all of the following prerequisites on your machine:
- Python 
- Python packages :
  - Requests : `pip install requests`
  - Beautiful Soup :  `pip install bs4`

## Usage

```
python sendcm_downloader.py [folder_link] [local_path]
```

- `folder_link`: The Folder URL 
- `local_path` [Optional] : the folder you want to save the file to, defaults to the current path
