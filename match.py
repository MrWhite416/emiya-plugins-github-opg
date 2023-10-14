import re
from libs.event.qqevent import onkeyword
import requests


BASEURL = "http://127.0.0.1:5700"
def sendGroupMsg(gid: int, text: str):

    d = {"message": text, "group_id": gid}
    requests.post(f"{BASEURL}/send_group_msg", data=d)


def extract(input_string):
    match = re.search(r'github\.com/([^/]+)/([^/]+)', input_string)

    if match:
        xxx = match.group(1)
        aaa = match.group(2)
        return xxx, aaa
    else:
        return None, None


def pic(one, two):
    pic_uri = f'https://opengraph.githubassets.com/0/{one}/{two}'

    return pic_uri


@onkeyword(keywordList=['github.com'])
def send_pic(pack):
    p_cq = f'[CQ:image,file={pic(*extract(pack.message))}]'
    sendGroupMsg(gid=pack.group_id, text=p_cq)




