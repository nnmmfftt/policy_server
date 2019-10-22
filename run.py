import sys
import perm_check
import model_build
import policy_paser
import
import os

class Request:
    def __init__(self):
        self.doc_token = None
        self.patient_id = None
        self.patient_token = None


    # 收到请求并且处理
    # todo: 与Go_rpc连接
    # 模拟收到的过程
    def receive(self, d, pid, ptk):
        self.doc_token = d
        self.patient_id = pid
        self.patient_token = ptk
        if self.doc_token & self.patient_id & self.patient_token == 1:
            return True
        else:
            return False


class Engine:
    def __init__(self):

    def decision(self):
        p = perm_check.PermissionCheck()
        rc = p.check(self.doc_token)
        if rc is True:
            model_build.Model.predict(pid, request)
        return





if __name__ == '__main__':
    doc_token = sys.argv[1]
    patient_id = sys.argv[2]
    patient_token = sys.argv[3]

    # permission check
    check = perm_check.PermissionCheck().check(ids=doc_token)
    if check is False:
        print("Doctor token invalid")
        sys.exit()

    # Got model
    model = model_build.Model.