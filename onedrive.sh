#!/bin/bash
pip install onedrivesdk
pip3 install git+https://github.com/OneDrive/onedrive-sdk-python.git
pip3 install --upgrade git+https://github.com/OneDrive/onedrive-sdk-python.git
echo "For Upload"
echo "- file: python onedrive.py upload file -i local_file/to/upload -o onedrive_path/to/save"
echo "- multi-files: python onedrive.py upload file -i local_file1/to/upload local_file/to/upload ... -o onedrive_path/to/save"
echo "- folder: python onedrive.py upload folder -i local_path/to/upload -o onedrive_path/to/save"
echo "For Download: "
echo "- file: python onedrive.py download file -i onedrive_file/to/download -o local_path/to/save"
echo "- multi-files: python onedrive.py download file -i onedrive_file1/to/download onedrive_file2/to/download... -o local_path/to/save"