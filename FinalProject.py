class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"


class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def read_doctors_file(self):
        try:
            with open("doctors.txt", "r") as file:
                for line in file:
                    parts = line.strip().split("_")
                    doctor_id, name, specialization, working_time, qualification, room_number = parts
                    doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
                    self.doctors.append(doctor)
        except FileNotFoundError:
            print("doctors.txt not found. Creating a new one.")

    def search_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def search_doctor_by_name(self, doctor_name):
        for doctor in self.doctors:
            if doctor.name == doctor_name:
                return doctor
        return None

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        self.write_doctors_file()

    def write_doctors_file(self):
        with open("doctors.txt", "a") as file:
            file.write(str(self.doctors[-1]) + "\n")


class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"


class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def read_patients_file(self):
        try:
            with open("patients.txt", "r") as file:
                for line in file:
                    parts = line.strip().split("_")
                    pid, name, disease, gender, age = parts
                    patient = Patient(pid, name, disease, gender, age)
                    self.patients.append(patient)
        except FileNotFoundError:
            print("patients.txt not found. Creating a new one.")

    def search_patient_by_id(self, pid):
        for patient in self.patients:
            if patient.pid == pid:
                return patient
        return None

    def add_patient(self, patient):
        self.patients.append(patient)
        self.write_patients_file()

    def write_patients_file(self):
        with open("patients.txt", "a") as file:
            file.write(str(self.patients[-1]) + "\n")


class Management:
    def display_main_menu(self):
        while True:
            print("Welcome to Alberta Hospital (AH) Management system")
            print("Select from the following options, or select 3 to stop:")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit Program")

            choice = input(">>> ")

            if choice == '1':
                self.doctors_submenu()
            elif choice == '2':
                self.patients_submenu()
            elif choice == '3':
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def doctors_submenu(self):
        doctor_manager = DoctorManager()

        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")

            choice = input(">>> ")

            if choice == '1':
                self.display_doctors_list(doctor_manager.doctors)
            elif choice == '2':
                self.search_doctor_by_id(doctor_manager)
            elif choice == '3':
                self.search_doctor_by_name(doctor_manager)
            elif choice == '4':
                self.add_doctor(doctor_manager)
            elif choice == '5':
                self.edit_doctor_info(doctor_manager)
            elif choice == '6':
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def patients_submenu(self):
        patient_manager = PatientManager()

        while True:
            print("\nPatients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")

            choice = input(">>> ")

            if choice == '1':
                self.display_patients_list(patient_manager.patients)
            elif choice == '2':
                self.search_patient_by_id(patient_manager)
            elif choice == '3':
                self.add_patient(patient_manager)
            elif choice == '4':
                self.edit_patient_info(patient_manager)
            elif choice == '5':
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def display_doctors_list(self, doctors):

        for doctor in doctors:
            print(f"{doctor.doctor_id:<5}{doctor.name:<23}{doctor.specialization:<15}{doctor.working_time:<15}{doctor.qualification:<15}{doctor.room_number}")

    def search_doctor_by_id(self, doctor_manager):
        doctor_id = input("Enter the doctor Id: ")
        doctor = doctor_manager.search_doctor_by_id(doctor_id)
        if doctor:
            self.display_doctors_list([doctor])
        else:
            print(f"Can't find the doctor with the ID {doctor_id} on the system")

    def search_doctor_by_name(self, doctor_manager):
        doctor_name = input("Enter the doctor name: ")
        doctor = doctor_manager.search_doctor_by_name(doctor_name)
        if doctor:
            self.display_doctors_list([doctor])
        else:
            print(f"Can't find the doctor with the name {doctor_name} on the system")

    def add_doctor(self, doctor_manager):
        doctor_id = input("Enter the doctor’s ID: ")
        name = input("Enter the doctor’s name: ")
        specialization = input("Enter the doctor’s specialization: ")
        working_time = input("Enter the doctor’s working time (e.g., 8am-5pm): ")
        qualification = input("Enter the doctor’s qualification: ")
        room_number = input("Enter the doctor’s room number: ")
        new_doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
        doctor_manager.add_doctor(new_doctor)
        print(f"Doctor whose ID is {doctor_id} has been added")

    def edit_doctor_info(self, doctor_manager):
        doctor_id = input("Please enter the id of the doctor that you want to edit their information: ")
        doctor = doctor_manager.search_doctor_by_id(doctor_id)
        if doctor:
            print(f"Editing Doctor with ID {doctor_id}")
            name = input("Enter new Name: ")
            specialization = input("Enter new Speciality in: ")
            working_time = input("Enter new Timing: ")
            qualification = input("Enter new Qualification: ")
            room_number = input("Enter new Room number: ")
            doctor.name = name
            doctor.specialization = specialization
            doctor.working_time = working_time
            doctor.qualification = qualification
            doctor.room_number = room_number
            print(f"Doctor whose ID is {doctor_id} has been edited")
            doctor_manager.write_doctors_file()
        else:
            print(f"Can't find the doctor with the ID {doctor_id} on the system")

    def display_patients_list(self, patients):
        
        for patient in patients:
            print(f"{patient.pid:<5}{patient.name:<23}{patient.disease:<15}{patient.gender:<15}{patient.age}")

    def search_patient_by_id(self, patient_manager):
        pid = input("Enter the Patient Id: ")
        patient = patient_manager.search_patient_by_id(pid)
        if patient:
            self.display_patients_list([patient])
        else:
            print(f"Can't find the Patient with the ID {pid} on the system")

    def add_patient(self, patient_manager):
        pid = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        new_patient = Patient(pid, name, disease, gender, age)
        patient_manager.add_patient(new_patient)
        print(f"Patient whose ID is {pid} has been added")

    def edit_patient_info(self, patient_manager):
        pid = input("Please enter the id of the Patient that you want to edit their information: ")
        patient = patient_manager.search_patient_by_id(pid)
        if patient:
            print(f"Editing Patient with ID {pid}")
            name = input("Enter new Name: ")
            disease = input("Enter new disease: ")
            gender = input("Enter new gender: ")
            age = input("Enter new age: ")
            patient.name = name
            patient.disease = disease
            patient.gender = gender
            patient.age = age
            print(f"Patient whose ID is {pid} has been edited")
            patient_manager.write_patients_file()
        else:
            print(f"Can't find the Patient with the ID {pid} on the system")


def main():
    management = Management()
    management.display_main_menu()


if __name__ == "__main__":
    main()
