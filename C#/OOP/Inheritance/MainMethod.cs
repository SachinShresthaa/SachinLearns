using System;
class MainMethod
{
    static void Main(String[] args)
    {
        Doctor d1 = new Doctor("sachin",22, "Heart" ,50000);
        d1.DisplayDoctorInfo();
        d1.DisplayPersonInfo();

        Patient p1 = new Patient("Angel",20,"Headache",7);
        p1.DisplayPatientInfo();
        p1.DisplayPersonInfo();
        
    }
}