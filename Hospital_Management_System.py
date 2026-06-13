from abc import ABC,abstractmethod
import json

def get_positive_int(massage):

        while True:

            try:
                value=int(input(massage))
                if value<=0:
                    print("Number Must Be Greater Than Zero (0) ! ")
                    continue
                return value
            except ValueError:
                print("Enter A Valid Number!")

def get_non_empty_string(massage):
        while True:
            try:
                value=input(massage).strip()
                if value==" ":
                    print("Values Can't Be Empty!")
                    continue
                return value
            except ValueError:
                print("Enter A Valid Input!")

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

class PatientReport(MedicalRecord):

    def __init__(self,patient):
        
        self.patient=patient

    def generate_report(self):        
        print("\n-------- PATIENT REPOST ----------")
        print(f"Patient's Name    : {self.patient.name}")
        print(f"Patient's Disease : {self.patient.disease}")
        print(f"Patient's Bill    : {self.patient.get_bill()}/-")
        print(f"Status            : {self.patient.status}")
        print("-" * 30)


class DoctorReport(MedicalRecord):

    def __init__(self,doctor):
        
        self.doctor=doctor

    def generate_report(self):
        
        print("\n------------ DOCTOR REPOST ----------------")
        print(f"Doctor's Name            : {self.doctor.name}")
        print(f"Doctor's speacialization : {self.doctor.specialization}")
        print(f"Doctor's salary          : {self.doctor.get_salary()}/-")
        print("-" * 30)


class Hospital:

    def __init__(self):
        self.patients=[]
        self.doctors=[]
        self.appointments=[]
        
        self.load_doctor()
        self.load_patient()
        self.load_appointment()

    def save_doctor(self):

        data=[]

        for doctor in self.doctors:
            data.append({
                "id":doctor.id,
                "name":doctor.name,
                "age":doctor.age,
                "specialization":doctor.specialization,
                "salary":doctor.get_salary()
                })
            
        with open("doctors.json","w")as file:
            json.dump(data,file,indent=4)

    def save_patient(self):

        data=[]

        for patient in self.patients:
            data.append({
                "id":patient.id,
                "name":patient.name,
                "age":patient.age,
                "disease":patient.disease,
                "bill":patient.get_bill(),
                "status":patient.status
            })

        with open("patients.json","w")as file:
            json.dump(data,file,indent=4)

    def save_appointment(self):

        data=[]

        for appointment in self.appointments:
            data.append({
                "app_id":appointment.app_id,
                "doctor_id":appointment.doctor_id,
                "patient_id":appointment.patient_id,
                "date":appointment.date,
                "time":appointment.time
            })

        with open("appointments.json","w")as file:
            json.dump(data,file,indent=4)



    def load_doctor(self):

        try:
            
            with open("doctors.json","r")as file:
                data=json.load(file)

                for doctor_data in data:
                    doctor=Doctor(
                        doctor_data["id"],
                        doctor_data["name"],
                        doctor_data["age"],
                        doctor_data["specialization"],
                        doctor_data["salary"]
                    )
                    
                    self.doctors.append(doctor)

        except FileNotFoundError:
            pass

    def load_patient(self):

        try:

            with open("patients.json","r")as file:
                data=json.load(file)

                for patient_data in data:
                    patient=Patient(
                        patient_data["id"],
                        patient_data["name"],
                        patient_data["age"],
                        patient_data["disease"],
                        patient_data["bill"],
                        patient_data["status"]
                    )
                    
                    self.patients.append(patient)

        except FileNotFoundError:
            pass

    def load_appointment(self):

        try:
            with open("appointments.json","r")as file:
                data=json.load(file)

                for appointment_data in data:
                    appointment=Appointment(
                        appointment_data["app_id"],
                        appointment_data["doctor_id"],
                        appointment_data["patient_id"],
                        appointment_data["date"],
                        appointment_data["time"]
                    )

                    self.appointments.append(appointment)

        except FileNotFoundError:
            pass
                                                                
    def add_patient(self,patient):

        self.patients.append(patient)
        self.save_patient()

    def add_doctor(self,doctor):

        self.doctors.append(doctor)
        self.save_doctor()

    def show_doctors(self):
        if not self.doctors:
            print("No Data Yet !")
            return
        
        for doctor in self.doctors:
            doctor.show_doctor()

    def show_patients(self):
        if not self.patients:
            print("No data Yet !")
            return
        for patient in self.patients:
            patient.show_patient()

    def generate_report(self):

        reports=[]

        for doctor in self.doctors:
            reports.append(DoctorReport(doctor))

        for patient in self.patients:
            reports.append(PatientReport(patient))

        for report in reports:
            report.generate_report()

    def update_patient_bill(self,id,new_bill):

        if not self.patients:
            print("No Data!")
            return
        
        for patient in self.patients:
            if patient.id==id:
                patient.set_bill(new_bill)
                self.save_patient()
                print("Updated Successfully ! ")
                return
        
        print("Patient Id Not Found !")

    def search_patient(self,id):
        if not self.patients:
            print("No Data Yet!")
            return
        for patient in self.patients:
            if patient.id==id:
                print("\n--- Patient Found ! ---\n")
                print(f"Name    : {patient.name}")
                print(f"Disease : {patient.disease}")
                print(f"Bill    : {patient.get_bill()}/-")
                print("-" * 30)
                return
        print("Patient Not Found!")

    def search_doctor(self,id):
        if not self.doctors:
            print("No Data Yet!")
            return
        for doctor in self.doctors:
            if doctor.id==id:
                print("\n----- Doctor Found ! -----\n")
                print(f"Name           : {doctor.name}")
                print(f"Specialization : {doctor.specialization}")
                print(f"Salary         : {doctor.get_salary()}/-")
                print("-" * 30)
                return
        print("Doctor Not Found ! ")

    def delete_patient(self,id):
        if not self.patients:
            print("No Data Yet!")
            return
        for patient in self.patients:
            if patient.id==id:
                self.patients.remove(patient)
                self.save_patient()
                print("Patient Deleted Successfully!")
                return
        print("Patient Not Found!")

    def delete_doctor(self,id):
        if not self.doctors:
            print("No Data Yet!")
            return
        for doctor in self.doctors:
            if doctor.id==id:
                self.doctors.remove(doctor)
                self.save_doctor()
                print("Doctor Deleted successfully!")
                return
        print("Doctor Not Found ! ")

    def admit_patient(self,id):

        admitted=0

        if not self.patients:
            print("No Patient Listed Yet !")
            return
        for patient in self.patients:
            if patient.id==id:
                patient.status="Admitted"
                admitted+=1
                self.save_patient()
                print("Patient Admitted!")
                return
        print("Patient Not Found!")

    def discharge_patient(self,id):

        discharge=0

        if not self.patients:
            print("No Patient Listed Yet !")
            return
        for patient in self.patients:
            if patient.id==id:
                patient.status="Discharged"
                discharge+=1
                admitted-=1
                self.save_patient()
                print("Patient Discharged!")
                return
        print("Patient Not Found!")

    def add_appointment(self,appointment):
        
        self.appointments.append(appointment)
        self.save_appointment()
        
        print("Appointment Successfully!")

    def show_appointment(self):

        if not self.appointments:
            print("No Appointment Yet!")
            return
        for i,appointment in enumerate(self.appointments,start=1):
            print("\n=========== Appointment List =============")
            print(f"\n------- Appointment {i} --------")
            appointment.show_appointment()
            print("-" * 30)

    def cancel_appointment(self,app_id):
        if not self.appointments:
            print("No Apoointment Data Yet!")
            return
        for appointment in self.appointments:
            if appointment.app_id==app_id:
                self.appointments.remove(appointment)
                self.save_appointment()
                print("Appointment Successfully Cancelled!")
                return
        print("Appointment not found!")

    def net_income(self):
        net_income=0
        for patient in self.patients:
            net_income+=patient.get_bill()
        return net_income
        
    def net_expense(self):
        net_expense=0
        for doctor in self.doctors:
            net_expense+=doctor.get_salary()
        return net_expense
        
    def net_profit(self):

        return self.net_income()-self.net_expense()
    
    def total_admitted(self):
        admitted=0
        for patient in self.patients:
            if patient.status=="Admitted":
                admitted+=1
        return admitted
        
    def total_discharged(self):
        discharged=0
        for patient in self.patients:
            if patient.status=="Discharged":
                discharged+=1
        return discharged
        

    def hospital_dashboard(self):

        print("\n========= Hospital Dashboard ===========")
        print(f"Doctors        : {len(self.doctors)}")
        print(f"Patients       : {len(self.patients)}")
        print(f"Admitted       : {self.total_admitted()}")
        print(f"Discharged     : {self.total_discharged()}")
        print(f"\n\nRevenue       : {self.net_income()}")
        print(f"Salary Expence : {self.net_expense()}")
        print(f"Profit         : {self.net_profit()}")
        print("-" * 30)

hospital=Hospital()
while True:

    print("\n-------- HOSPITAL MANAGEMENT SYSTEM ----------")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. show Doctors")
    print("4. Show Patients")
    print("5. Generate Reports")
    print("6. Update Patient Bill")
    print("7. Search Patient")
    print("8. Search Doctors")
    print("9. Delete Patient")
    print("10. Delete Doctor")
    print("11. Admit Patient")
    print("12. Discharge Patient")
    print("13. Make Appointment")
    print("14. Show All Appointments")
    print("15. Cancel Appointment")
    print("16. Hospital Dashboard")
    print("17. Exit")

    choice=get_positive_int("Enter Your choice Here : ")

    if choice==1:

        id=get_positive_int("Enter Patient's Id : ")
        name=get_non_empty_string("Enter Patients's Name : ")
        age=get_positive_int("Enter Patient's Age : ")
        disease=get_non_empty_string("Enter Patient's disease : ")
        bill=get_positive_int("Enter Patient's Bill : ")
        status="Null"

        patient=Patient(id,name,age,disease,bill,status)

        hospital.add_patient(patient)

        print("Patient Added successfully!")
    elif choice==2:

        id=get_positive_int("Enter Doctor's Id : ")
        name=get_non_empty_string("Enter Doctor's Name : ")
        age=get_positive_int("Enter Doctor's Age : ")
        specialization=get_non_empty_string("Enter Doctor's Specialization : ")
        salary=get_positive_int("Enter Doctor's Salary : ")

        doctor=Doctor(id,name,age,specialization,salary)
        hospital.add_doctor(doctor)
        print("Doctor Added Successfully!")

    elif choice==3:

        print("\n-------Doctors List--------")
        hospital.show_doctors()

    elif choice==4:

        print("\n-------Patients List--------")
        hospital.show_patients()

    elif choice==5:

        hospital.generate_report()

    elif choice==6:

        id=get_positive_int("Enter Patient's Id : ")
        new_bill=get_positive_int("Enter The New Bill Amount : ")

        hospital.update_patient_bill(id,new_bill)

    elif choice==7:
        id=get_positive_int("Enter Patient's Id : ")
        hospital.search_patient(id)

    elif choice==8:
        id=get_positive_int("Enter Doctor's Id : ")
        hospital.search_doctor(id)

    elif choice==9:
        id=get_positive_int("Enter Patient's id : ")
        hospital.delete_patient(id)

    elif choice==10:
        
        id=get_positive_int("Enter doctor's Id : ")
        hospital.delete_doctor(id)

    elif choice==11:

        id=get_positive_int("Enter Patient's ID To Admit : ")
        hospital.admit_patient(id)

    elif choice==12:

        id=get_positive_int("Enter Patient's ID To Discharge : ")
        hospital.discharge_patient(id)

    elif choice==13:

        app_id=get_positive_int("Enter Appointment ID : ")
        doctor_id=get_positive_int("Enter Doctor's ID : ")
        patient_id=get_positive_int("Enter Patient's ID : ")
        date=get_non_empty_string("Enter Date : ")
        time=get_non_empty_string("Enter Time : ")

        appointment=Appointment(app_id,doctor_id,patient_id,date,time)

        hospital.add_appointment(appointment)

    elif choice==14:

        hospital.show_appointment()

    elif choice==15:

        app_id=get_positive_int("Enter Your Appointment ID No. : ")

        hospital.cancel_appointment(app_id)

    elif choice==16:

        hospital.hospital_dashboard()

    elif choice==17:
        print("\n----Good Bye ! -----")
        break
    else:
        print("Invalid Choice ! \n--- Try Again ---")