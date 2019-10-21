import pyotp
import sys
import policy_comp

tag_mp = {'1':"JBSWY3DPEHPK3PXP"}
doc_dict = {}


class TimeCheck:
    def __init__(self):
        equl = False
        userid = None
        tag_received = None

    def compare(self, userid, tag_received):
        exist_tag = tag_mp[userid]
        received_tag = tag_received
        exist = pyotp.TOTP(exist_tag)
        received = pyotp.TOTP(received_tag)
        equl = exist.now() == received.now()
        return equl


class PermissionCheck:
    def __init__(self):
        idnum = None

    def check(self, idNum):
        try:
            exist = doc_dict[idNum]
            return exist
        except KeyError:
            return None


if __name__ == '__main__':
    # using
    # python file.py docid patientid totp
    docID = sys.argv[1]
    c = PermissionCheck()
    comp = c.check(docID)
    if comp is None:
        print("Invalid doc info")
    else:
        userID = sys.argv[2]
        tag = sys.argv[3]
        t = TimeCheck()
        result = t.compare(userid=userID, tag_received=tag)
        print(result)


    policy_comp.pred_max(input_file, out)




