public class Hospital
{
    List<Doctor> doctors = new List<Doctor>();
    List<Patient> patients = new List<Patient>();
    Dictionary<int,Patient> patientRecord = new Dictionary<int, Patient>();
        public void addDoctor(Doctor doctor)
    {
        doctors.Add(doctor);
        Console.WriteLine("Docter added successfully");
    }
    public void addPatient(int patientID,Patient patient)
    {
        patients.Add(patient);
        patientRecord.Add(patientID,patient);
        Console.WriteLine("Patient Added");
    }
    public void showDoctor()
    {
        foreach(Doctor d in doctors)
        {
            Console.WriteLine("");
            d.DisplayInfo();
        }
    }
    public void showPatient()
    {
        foreach(Patient p in patients)
        {
            Console.WriteLine("");
            p.DisplayInfo();
        }
    }
}