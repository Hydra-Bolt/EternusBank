# # # filling_data = ["Full Name", "Account Name", "CNIC", "Phone Number", "Account Type"]
# # # list_of_data = [self.fullname.text(),self.account_name.text(), self.cnic.text(), self.phone_number.text(),self.accountType.currentText()]
# # # info ={}
# # # if any([True if i=="" else False for i in list_of_data]):
# # #     print(f"{filling_data[list_of_data.index(True)]}")
# # # else:
# # #     for i in range(len(list_of_data)):
# # #         info[filling_data[i]] = list_of_data[i]


# # class A:
# #     def ___init___(self,name) -> None:
# #         print(2)
# # class B:
# #     def ___init___(self,id) -> None:
# #         print(3)
        
# # class C(A,B):
# #     def ___init___(self,name,id) -> None:
# #         super().___init___(name)
# #         super(B).___init___(id)
# # c = C(2,3)

# class Hospital:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

#     def print_info(self):
#         print('Name:', self.name)
#         print('Address:', self.address)

#     def print_hos_info(self):
#         print('HOSPITAL INFO')
#         self.print_info()


# class Doctor(Hospital):
#     def __init__(self, name, address, specialization):
#         super().__init__(name, address)
#         self.specialization = specialization

#     def print_doctor_info(self):
#         print("DOCTOR INFO")
#         super().print_info()
#         print('Specialization:', self.specialization)


# class Patient(Hospital):
#     def __init__(self, name, address, disease):
#         super().__init__(name, address)
#         self.disease = disease

#     def print_patient_info(self):
#         print("PATIENT INFO")
#         super().print_info()
#         print('Disease:', self.disease)


# class Medical_Test(Doctor, Patient):
#     def __init__(self, d_name, d_add, specialization, p_name, p_add, disease, test_name):
#         Doctor.__init__(self, d_name, d_add, specialization)
#         self.disease = disease
#         Patient.__init__(self, p_name, p_add, disease=self.disease)
#         self.test_name = test_name

#     def print_test_info(self):
#         print('MEDICAL TEST REPORT\nTEST NAME:', self.test_name)
#         Doctor.print_doctor_info(self)
#         Patient.print_patient_info(self)


# h = Hospital('AL-MUMTAZ', 'KALABOARD')
# h.print_hos_info()
# d = Doctor('DR.XYZ', 'MALIR', 'NEUROLOGY')
# d.print_doctor_info()
# p = Patient('MR.XYZ', 'NAZIMABAD', 'BRAIN TUMOR')
# p.print_patient_info()
# m = Medical_Test('DR.XYZ', 'MALIR', 'NEUROLOGY', 'MR.XYZ',
#                  'NAZIMABAD', 'BRAIN TUMOR', 'MRI')
# m.print_test_info()

hehe = {"hee":1}
print(hehe.update({2:3}))
print(hehe)