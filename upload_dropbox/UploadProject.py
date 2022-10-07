import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.ApwhGURgMQT1AYjorYxX5RS1136afbQSS0-Jy7ErEPFw-dLkC5bhPMVsetPlBAGmQkWBewNr-k4qY-j7fveUe3NWLWinl8L1ipGwB9QJgotjDSSsD7MCknexcuex7OKFgO3911M'
    transferData = TransferData(access_token)

    file_from = '"C:/Users/anvee/Pictures/my_wallpapers/BlackBg.png"'
    # The full path to upload the file to, including the file name
    file_to = '/school_work/images/BlackBg.png'

    # API v2
    transferData.upload_file(file_from, file_to)


main()
