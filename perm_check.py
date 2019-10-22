# -*- coding: utf-8 -*-
__author__ = 'hiqex'
import pyotp
import sys
import policy_comp

tag_mp = {'1':"JBSWY3DPEHPK3PXP"}
doc_dict = {}


class TimeCheck:
    def __init__(self):
        self.equal = False
        self.userid = None
        tag_received = None

    def compare(self, userid, tag_received):
        exist_tag = tag_mp[userid]
        received_tag = tag_received
        exist = pyotp.TOTP(exist_tag)
        received = pyotp.TOTP(received_tag)
        self.equal = exist.now() == received.now()
        return self.equal


class PermissionCheck:
    def __init__(self, ids=None):
        self.idNum = ids
        self.exist = False

    def check(self, ids=None):
        if ids is None:
            return self.exist
        try:
            self.exist = doc_dict[self.idNum]
            self.exist = True
            return self.exist
        except KeyError:
            return self.exist


if __name__ == '__main__':
    # using
    # python file.py docid patientid totp
    docID = sys.argv[1]
    comp = PermissionCheck().check(docID)
    if comp is None:
        print("Invalid doc info")
    else:
        userID = sys.argv[2]
        tag = sys.argv[3]
        t = TimeCheck()
        result = t.compare(userid=userID, tag_received=tag)
        print(result)





