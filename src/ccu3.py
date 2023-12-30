import datetime
import io
import requests
import urllib3
from urllib.parse import urlparse
from urllib.parse import parse_qs
from minio import Minio
from dotenv import load_dotenv
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

MINIO_HOST = os.getenv('MINIO_HOST')
MINIO_BUCKET = os.getenv('MINIO_BUCKET')
ACCESS_KEY = os.environ.get('MINIO_ACCESS_KEY')
SECRET_KEY = os.environ.get('MINIO_SECRET_KEY')
# tbUsernameShow = os.environ.get('tbUsernameShow')
tbUsername = os.environ.get('HOMEMATIC_USERNAME')
tbUsernameShow = tbUsername
tbPassword = os.environ.get('HOMEMATIC_PASSWORD')
HOMEMATIC_HOST = os.environ.get("HOMEMATIC_HOST")


def getUserToken():
    r = requests.post(HOMEMATIC_HOST + "/login.htm",
                      data={"tbUsernameShow": tbUsernameShow, "tbUsername": tbUsername, "tbPassword": tbPassword},
                      verify=False,
                      allow_redirects=False)
    # print(r.text)
    # print(r.headers["Location"])
    url = r.headers["Location"]
    parsed_url = urlparse(url)
    captured_value = parse_qs(parsed_url.query)['sid'][0]
    # print(captured_value)
    return captured_value


def getBackupRequest(sid):
    dl_url = HOMEMATIC_HOST + "/config/cp_security.cgi?sid=" + sid + "&action=create_backup"
    r2 = requests.get(dl_url, verify=False)
    return r2


def uploadToMinio(filename, content, content_length):
    MINIO_CLIENT = Minio(MINIO_HOST, access_key=ACCESS_KEY, secret_key=SECRET_KEY)
    value_as_a_stream = io.BytesIO(content)
    try:
        res = MINIO_CLIENT.put_object(MINIO_BUCKET, object_name=filename, data=value_as_a_stream,
                                      length=int(content_length), )  # content_type="application/x-download",
    except Exception as e:
        print("Error :: Saving Backup locally.")
        print(e)
        open(filename, "wb").write(content)

    # DEBUG PRINT / LOGGING
    # for attr in dir(res):
    #    # Getting rid of dunder methods
    #    if not attr.startswith("__"):
    #        print(attr, getattr(res, attr))


def runSchedule():
    print("\n\nStarting Backup Job at :: {}".format(datetime.datetime.today()))
    print("Getting User Token")
    sid = getUserToken()
    print("Starting backup request with user token.")
    backupRequest = getBackupRequest(sid)
    filename = backupRequest.headers["Content-Disposition"].split("filename=")[1]
    print("Uploading file to Minio")
    uploadToMinio(filename, backupRequest.content, backupRequest.headers["Content-Length"])
    print("Upload Done. Backup Task finished")
    print("Ending Job at :: {}".format(datetime.datetime.today()))
    print("\n\n")
