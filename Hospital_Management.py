class patient:
    def __init__(self,Name,Age,Specialist,Address,Contact):  
        self.name=Name
        
        self.age=Age
        
        self.specialist=Specialist
        
        self.address=Address
        
        self.contact=Contact
    
    def display(self):
        print("Patient's Name",self.name,"\nPatient's Age",self.age,"\nPatient's Disease",self.specialist,"\nPatient's Address",self.address,"\nPatient's Contact",self.contact)

class Hospital:
    def __init__(self,Name,Icu_count,Emergency_count,General_count,Doctor_availability):  
        self.name= Name
        self.icu_count = Icu_count
        self.emergency_count=Emergency_count
        self.general_count=General_count
        self.doctor_availability = Doctor_availability
    
    def display(self):
        print("Hospital Name",self.name,"\nicu_count",self.icu_count,"\nEmergency_count",self.emergency_count,"\nGeneral_count",self.general_count,"\nDoctor's availabiltiy",self.doctor_availability)
  
Hospital_details = Hospital("XYZ_HOSPITAL",5,2,10,100)
Hospital_details.display()

print("\n")

print("###################################### Get patient details ######################################")

print("\n")

print("\n")

print("*****************SPECIALIST DETAILS : Ortho , Dental, Neuro, General, Physio, Opthomologist, Gestro, Cardio***************** ")

print("\n")

patientDetail = patient(input("Enter Patient Name "),input("Enter Age "),input("Enter specialist "),input("Enter Address "),input("Enter contact "))

print("\n")

print("\n")

print("****************************** Patient Details *****************************")

patientDetail.display()



print("###################################### your Specialist doctor ######################################")

print("\n")

doctors = {"Ortho": {"name": "DR Kalaivanan", "Room no": 1},
            "Dental": {"name": "DR Evine Mathew", "Room no": 2},
            "Neuro": {"name": "DR Abhi", "Room no": 3},
            "General": {"name": "DR Abhilash", "Room no": 4},
            "Opthomologist": {"name": "DR Diwakar", "Room no": 5},
            "Physio": {"name": "DR Shalini ", "Room no": 6},
            "Gestro": {"name": "DR Vaidiyanathan ", "Room no": 7},
            "Cardio": {"name": "DR Agarwal ", "Room no": 8}}


if patientDetail.specialist in doctors:
    string = ""
    for key, value in doctors[patientDetail.specialist].items():
        string += key + " " + str(value) + " "
    print(string)
    
    print("\n")
    
    print("  You are perfectly all right   ")