# 🐱‍Install environment

 - win:
 
   ```
   pip install onedrivesdk
   pip3 install git+https://github.com/OneDrive/onedrive-sdk-python.git
   pip3 install --upgrade git+https://github.com/OneDrive/onedrive-sdk-python.git
   ```
   
 - ubuntu: 
 
   ```
   sh onedrive.sh
   ```
   
# 🐱‍Copy your client_id,client_secret to authen() function
   
   read: https://blog.csdn.net/sleepinghm/article/details/118991143
   
# 🐱‍Run!

 - For Upload:
 
    - single-file:
    
    `python onedrive.py upload file -i local_file/to/upload -o onedrive_path/to/save`
    
    - multi-files:

    `python onedrive.py upload file -i local_file1/to/upload local_file/to/upload ... -o onedrive_path/to/save`
    
    - folder:
    
    `python onedrive.py upload folder -i local_path/to/upload -o onedrive_path/to/save`
    
 - For Download: 
 
    - single-file:
    
     `python onedrive.py download file -i onedrive_file/to/download -o local_path/to/save`
     
    - multi-files:
    
     `python onedrive.py download file -i onedrive_file1/to/download onedrive_file2/to/download... -o local_path/to/save`

# supplement

 - /file/to/... : absolute path including file extension, such as: floder/file.txt 
 
 - /path/to/... : absolute path, such as: floder/ 
