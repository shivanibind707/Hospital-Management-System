from hospital import Hospital
from models import Patient,Doctor,Appointment
from utils import get_non_empty_string,get_positive_int

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