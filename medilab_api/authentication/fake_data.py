from faker import Faker
fake = Faker()

# Generar datos de ejemplo para el modelo Role
roles = ['ADMIN', 'DOCTOR', 'PATIENT', 'COMPANY']

# Generar datos de ejemplo para el modelo User
# Generar datos de ejemplo para el modelo User
users = []
for _ in range(10):
    user = {
        "role": fake.random_element(["ADMIN", "DOCTOR", "PATIENT", "COMPANY"]),
        "identification_type": "ID",
        "identification_number": fake.unique.random_number(),
        "phone": fake.phone_number(),
        "email": fake.email(),
        "date_of_birth": fake.date_of_birth(),
        "department": fake.city(),
        "city": fake.city(),
        "address": fake.address(),
        "gender": fake.random_element(["Male", "Female"]),
        "last_login_ip": fake.ipv4(),
        # Agrega otros campos aquí según tus necesidades
    }
    users.append(user)

# Generar datos de ejemplo para el modelo Doctor
doctors = []
for user_data in users:
    doctor = {
        "user": user_data,
        "specialty": fake.random_element(["Cardiology", "Dermatology", "Pediatrics"]),
        # otros campos aquí
    }
    doctors.append(doctor)

# Generar datos de ejemplo para el modelo Patient
patients = []
for user_data in users:
    patient = {
        "user": user_data,
        "profile_picture": fake.image_url(),
        # otros campos aquí
    }
    patients.append(patient)
