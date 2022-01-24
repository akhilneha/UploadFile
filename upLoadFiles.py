import dropbox

class TransferData:
    def _init_(self,access_token):
        self.access_token=access_token

    def upload_File(self,file_from,file_to):
        dbx = dropbox.Dropbox(acces_token)   

        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.BAv-zgc3lzMfnT3mLuzy7kaOdfyduPHZzbGjCCdHQKOTr4u6QkN63VVeUEudB2wDQEK0rLQl2dwWso4LSknXMVsVFUTu6q1t2ASfWBN_NFsnFThI0sGcK4gA8CB5gl6eUPlRjWk"
    transferData=TransferData(access_token)
    file_from=input("Enter the file name which you want to be transfer")
    file_to=input("Enter the path to upload in dropbox")
    transferData.upload_Files(file_from,file_to)
    print("File has been moved")           