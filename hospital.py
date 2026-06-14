import json
from models import Patient,Doctor,Appointment
from reports import PatientReport,DoctorReport

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