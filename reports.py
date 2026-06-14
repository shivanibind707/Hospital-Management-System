from models import MedicalRecord

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