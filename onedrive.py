import argparse
import onedrivesdk
import os

def authen():
    redirect_uri = 'https://od.cnbeining.com'
    client_secret = 'your_client_secret'
    client_id = 'your_client_id'
    api_base_url = 'https://api.onedrive.com/v1.0/'
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

    http_provider = onedrivesdk.HttpProvider()
    auth_provider = onedrivesdk.AuthProvider(
        http_provider=http_provider,
        client_id=client_id,
        scopes=scopes)

    client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)
    # Ask for the code
    print('Paste this URL into your browser, approve the app\'s access.')
    print('Copy everything in the address bar after "code=", and paste it below.')
    print(auth_url)
    code = input('Paste code here: ')  # M.R3_BAY.153e2421-da6c-e47b-b233-ca56f17d960c
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    return client


if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog='for onedrive')
    parse.add_argument('flag1', help='upload/download', type=str)
    parse.add_argument('flag2', help='file/folder', type=str)
    parse.add_argument('-i', '--input', help='input file path', nargs='+')
    parse.add_argument('-o', '--output', help='save path', type=str)
    opt = parse.parse_args()
    print(opt)
    client = authen()
    if opt.flag2 == 'file':
        for inputfile in opt.input:
            filename = os.path.basename(inputfile)
            savefile = os.path.join(opt.output, filename)
            if opt.flag1 == 'upload':
                client.item(drive='me', path=savefile).upload(inputfile)
                print("uploading file from %s to onedrive/%s " % (inputfile, savefile))
            elif opt.flag1 == 'download':
                os.makedirs(opt.output, exist_ok=True)
                client.item(drive='me', path=inputfile).download(savefile)
                print("downloading file from onedrive/%s to %s " % (inputfile, savefile))
            else:
                print("input error:file/folder')
    elif opt.flag2 == 'folder':
        for inputfolder in opt.input:
            for root, _, files in os.walk(inputfolder, topdown=False):
                for name in files:
                    input_file = os.path.join(root, name)
                    save_file = os.path.join(opt.output, input_file.strip(inputfolder))
                    if opt.flag1 == 'upload':
                        client.item(drive='me', path=save_file).upload(input_file)
                        print("uploading folder from %s to onedrive/%s " % (input_file, save_file))
                    else:
                        print("please input:'upload'")
    else:
        print("input error:upload/download")
