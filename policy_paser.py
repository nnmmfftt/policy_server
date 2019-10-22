import sys


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


class Policy:
    def __init__(self, patient_id=None, doctor=Doctor(), decision=False):
        self.pid = patient_id
        self.doctor = doctor
        self.decision = decision

    def new_policy(self, patient_id: 'int', doctor: 'Doctor', decision: 'bool'):
        self.pid = patient_id
        self.doctor = doctor
        self.decision = decision
        return self

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
    def __init__(self, patient_id=None, patient_birth=None, gender=None, disease=None):
        self.patient_id = patient_id
        self.patient_birth = patient_birth
        self.gender = gender
        self.disease = [] if disease is None else self.disease.append(disease)

    def new_patient(self, patient_id: 'int', patient_birth: 'int', gender: 'int'):
