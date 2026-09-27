public class Hospital
{
    List<Doctor> doctors = new List<Doctor>();
    List<Patient> patients = new List<Patient>();
    Dictionary<int, Patient> patientRecord = new Dictionary<int, Patient>();
    public void AddDoctor(Doctor doctor)
    {
        doctors.Add(doctor);
        Console.WriteLine("Doctor added successfully");
    }
    public void AddPatient(int patientID, Patient patient)
    {
        patients.Add(patient);
        patientRecord.Add(patientID, patient);
        Console.WriteLine("Patient Added");
    }
    public void ShowDoctor()
    {
        foreach(Doctor d in doctors)
        {
            Console.WriteLine("");
            d.DisplayInfo();
        }
    }
    public void ShowPatient()
    {
        foreach(Patient p in patients)
        {
            Console.WriteLine("");
            p.DisplayInfo();
        }
    }
}