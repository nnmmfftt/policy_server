import sys
import _pickle as cPickle


class Doctor:
    def __init__(self, doctor_id=None, part_id=None, level= None):
        self.doctor_id = doctor_id
        self.part_id = part_id
        self.level = level

    def new_doctor(self, doctor_id=None, part_id=None, level= None):
        if doctor_id & part_id & level != 0:
            return True
        self.doctor_id = doctor_id
        self.part_id = part_id
        self.level = level


class Patient:
    # 病人信息
    # @patient_id
    # 病人id编号
    # @patient_birth
    # 病人的生日, 8位数字
    # @gender
    # 性别: 0、未知, 1、男, 2、女
    # @disease
    # 疾病信息,dict,{disease_name:str}
    # 保存着疾病名称与相关诊断描述
    def __init__(self, patient_id=None, patient_birth=None, gender=None, disease=None, patient_file = 'patient_file'):
        self.patient_id = patient_id
        self.patient_birth = patient_birth
        self.patient_file = patient_file
        self.gender = gender
        self.disease = [] if disease is None else self.disease.append(disease)
        try:
            f = open(patient_file, 'rb')
        except FileNotFoundError:
            print("patient info file open error, check the file")
            self.patient_dict = {}
        else:
            self.patient_dict = cPickle.load(f)

    def new_patient(self, patient_id: 'int', patient_birth: 'int', gender: 'int', disease: 'dict'):
        self.patient_id = patient_id
        self.patient_birth = patient_birth
        self.gender = gender
        if len(self.patient_dict) > 0:
            t = iter(disease).__next__()
            self.patient_dict[patient_id][t] = disease[t]
        self.save_patient()

    def set_filename(self, file_name: 'str'):
        self.patient_file = file_name

    def save_patient(self):
        save_name = self.patient_file + '.pkl'
        cPickle.dump(self.patient_dict, open(save_name, 'w'), cPickle.HIGHEST_PROTOCOL)


class Policy:
    def __init__(self, patient=Patient(), doctor=Doctor(), decision=False):
        self.patient_id = patient.patient_id
        self.doctor = doctor
        self.decision = decision

    def new_policy(self, patient_id: 'int', doctor: 'Doctor', decision: 'bool'):
        self.patient_id = patient_id
        self.doctor = doctor
        self.decision = decision
        return self


class PolicyParser:

    def __init__(self, policy: 'Policy'):
        self.patient_id = policy.patient_id
        self.doctor_id = policy.doctor.doctor_id
        self.doctor_lv = policy.doctor.level
        self.decision = policy.decision
        self.doctor_part = policy.doctor.part_id

    def paser_policset(self):
        self.doctor_id

