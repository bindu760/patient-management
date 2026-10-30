from fastapi import APIRouter, HTTPException, status

from app.database import load_patients, save_patients
from schemas.patient import PatientCreate, PatientUpdate


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


# CREATE PATIENT
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient(patient: PatientCreate):

    patients = load_patients()

    new_id = max(
        (p["id"] for p in patients),
        default=0
    ) + 1

    new_patient = patient.model_dump()
    new_patient["id"] = new_id

    patients.append(new_patient)
    save_patients(patients)

    return {
        "message": "Patient created successfully",
        "data": new_patient
    }


# GET ALL PATIENTS
@router.get("/")
def get_all_patients():

    patients = load_patients()

    return {
        "total": len(patients),
        "patients": patients
    }


# GET PATIENT BY ID
@router.get("/{patient_id}")
def get_patient(patient_id: int):

    patients = load_patients()

    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Patient not found"
    )


# UPDATE PATIENT
@router.put("/{patient_id}")
def update_patient(patient_id: int, updated_data: PatientUpdate):

    patients = load_patients()

    for patient in patients:

        if patient["id"] == patient_id:

            changes = updated_data.model_dump(exclude_unset=True)

            patient.update(changes)

            save_patients(patients)

            return {
                "message": "Patient updated successfully",
                "data": patient
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Patient not found"
    )


# DELETE PATIENT
@router.delete("/{patient_id}")
def delete_patient(patient_id: int):

    patients = load_patients()

    for patient in patients:

        if patient["id"] == patient_id:

            patients.remove(patient)
            save_patients(patients)

            return {
                "message": "Patient deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Patient not found"
    )