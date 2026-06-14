from abc import ABC ,abstractmethod
class Person:

    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    def show_detail(self):

        print(f"ID       : {self.id}")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")

class Patient(Person):

    def __init__(self,id, name, age,disease,bill,status):
        super().__init__(id, name, age)
        self.disease=disease
        self.__bill=bill
        self.status=status

    def get_bill(self):
        return self.__bill
    
    def set_bill(self,new_bill):
        self.__bill=new_bill

    def show_patient(self):

        super().show_detail()
        print(f"Disease  : {self.disease}")
        print(f"Bill     : {self.__bill}/-")
        print(f"Status   : {self.status}")
        print("-" * 30)

class Doctor(Person):

    def __init__(self,id, name, age,specialization,salary):
        super().__init__(id, name, age)
        self.specialization=specialization
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def show_doctor(self):

        super().show_detail()
        print(f"Specialization : {self.specialization}")
        print(f"Salary         : {self.__salary}/-")
        print("-" * 30)


class Appointment:
    
    def __init__(self,app_id,doctor_id,patient_id,date,time):
        self.app_id=app_id
        self.doctor_id=doctor_id
        self.patient_id=patient_id
        self.date=date
        self.time=time

    def show_appointment(self):
        print(f"Appointment ID : {self.app_id}")
        print(f"Doctor ID      : {self.doctor_id}")
        print(f"Patient ID     : {self.patient_id}")
        print(f"Date           : {self.date}")
        print(f"Time           : {self.time}")
        

class MedicalRecord(ABC):

    @abstractmethod
    def generate_report(self):
        pass