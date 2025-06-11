import streamlit as st

# Title
st.set_page_config(page_title="Sehat-Khoj", layout="centered")
st.title("Welcome to Sehat-Khoj")
st.subheader("Select your role to continue")

# Role Selection
role = st.selectbox("Choose your role:", ["-- Select --", "Patient", "Doctor", "Caretaker"])

# Form for Patient
if role == "Patient":
    st.header("Patient Registration")
    with st.form("patient_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        occupation = st.text_input("Occupation")
        state = st.text_input("State")
        city = st.text_input("City")
        district = st.text_input("District")
        hospital_type = st.selectbox("Hospital Type", ["Government", "Private"])
        hospital_name = st.text_input("Name of Hospital")
        admission_date = st.date_input("Date of Admission")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(f"Patient profile saved for {name}!")

# Form for Doctor
elif role == "Doctor":
    st.header("Doctor Registration")
    with st.form("doctor_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=20)
        reg_no = st.text_input("Medical Registration Number")
        qualification = st.selectbox("Qualification", ["MBBS", "Post-graduate"])
        department = st.text_input("Department")
        hospital_type = st.selectbox("Hospital Type", ["Government", "Private"])
        hospital_name = st.text_input("Name of Hospital")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(f"Doctor profile saved for Dr. {name}!")

# Form for Caretaker
elif role == "Caretaker":
    st.header("Caretaker Registration")
    with st.form("caretaker_form"):
        name = st.text_input("Caretaker Name")
        patient_name = st.text_input("Name of Patient")
        relation = st.text_input("Relation to Patient")
        age = st.number_input("Age", min_value=0)
        occupation = st.text_input("Occupation")
        state = st.text_input("State")
        city = st.text_input("City")
        district = st.text_input("District")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(f"Caretaker profile saved for {name} caring for {patient_name}!")

# Conditions
if role in ["Patient", "Doctor", "Caretaker"]:
    st.markdown("---")
    st.header("Choose a condition to monitor")
    condition = st.selectbox("Condition", ["-- Select --", "Hypertension", "Diabetes", "Tuberculosis", "Pregnancy Care", "Child Care and Vaccination"])

    if condition == "Hypertension":
        with st.form("htn_form"):
            date = st.date_input("Date")
            time = st.time_input("Time")
            bp = st.text_input("BP Reading (e.g., 120/80)")
            meds = st.text_area("Medications List")
            meds_taken = st.selectbox("Medications Taken Today?", ["Yes", "No"])
            complaints = st.text_area("Any Health Complaints or Side Effects")
            submitted = st.form_submit_button("Save Entry")
            if submitted:
                st.success("Hypertension log saved!")

    elif condition == "Diabetes":
        with st.form("dm_form"):
            date = st.date_input("Date")
            time = st.time_input("Time")
            sugar = st.text_input("Blood Sugar Level (mg/dL)")
            meds = st.text_area("Medications List")
            meds_taken = st.selectbox("Medications Taken Today?", ["Yes", "No"])
            complaints = st.text_area("Any Health Complaints or Side Effects")
            submitted = st.form_submit_button("Save Entry")
            if submitted:
                st.success("Diabetes log saved!")

    elif condition == "Tuberculosis":
        with st.form("tb_form"):
            start_date = st.date_input("Treatment Started From")
            today = st.date_input("Today's Date")
            meds_taken = st.selectbox("Medications Taken Today?", ["Yes", "No"])
            complaints = st.text_area("Any Health Complaints or Side Effects")
            submitted = st.form_submit_button("Save Entry")
            if submitted:
                st.success("TB log saved!")

    elif condition == "Pregnancy Care":
        with st.form("pregnancy_form"):
            lmp = st.date_input("Last Menstrual Period (LMP)")
            tabs_taken = st.text_area("Tablets Taken")
            diet = st.text_area("Dietary Intake")
            complaints = st.text_area("Any Health Complaints or Side Effects")
            submitted = st.form_submit_button("Save Entry")
            if submitted:
                st.success("Pregnancy care log saved!")

    elif condition == "Child Care and Vaccination":
        with st.form("childcare_form"):
            name = st.text_input("Child's Name")
            age = st.number_input("Age (months)", min_value=0.0)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            height = st.number_input("Height/Length (cm)")
            weight = st.number_input("Weight (kg)")
            muac = st.number_input("Mid-upper Arm Circumference (cm)")
            vax = st.text_input("Recent Vaccination & Dose")
            if age < 48:
                st.markdown("### Developmental Milestones")
                crawling = st.selectbox("Crawling/Walking Milestone", ["Achieved", "Not yet"])
                holding = st.selectbox("Object Holding Milestone", ["Achieved", "Not yet"])
                social = st.selectbox("Social Milestone", ["Achieved", "Not yet"])
                language = st.selectbox("Language Milestone", ["Achieved", "Not yet"])
            complaints = st.text_area("Any Health Complaints")
            submitted = st.form_submit_button("Save Entry")
            if submitted:
                st.success("Child care entry saved!")