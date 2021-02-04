import cv2 as cv2
import dropbox
import time
import random
start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    # initializing cv2
    video_capture_obj = cv2.VideoCapture(0)
    result = True

    while(result):
        # read the frame while the camera is on
        ret, frame = video_capture_obj.read()
        # cv2.imwrite() is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False

    return img_name
    print('snapshot taken')
    # releases the camera
    video_capture_obj.release()
    # close all window that might be open for this process
    cv2.destroyAllWindows()
    
def upload_file(img_name):
    access_token = 'sl.AqQCCsWdZX_dBVCjGLuXdTFbhyYZ1C7nzCiCjtyA3zrlv77tHX5duWgpTbNEnzLJgQTM-53qKTX6yOpcDQK-jd-MaGflhTV7xFMtr1vWer76xUaCVAH7VXuY3DUEjApZYAXMhcY'
    # The full path to upload the file to, including the file name
    file = img_name
    file_from = file
    file_to = "/securityCheck/images"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,
                         mode=dropbox.files.WriteMode.overwrite)
    # API v2
        print('files uploaded')

def main():
    while(True):
        if((time.time()-start_time)>=5):
            print(time.time(),start_time)
            name = take_snapshot()
            upload_file(name)

main()
