using System.Runtime.CompilerServices;
using System.Security.Cryptography;

class Doctor : Person
{
    private int DoctorID;
    private string Specialization="";
    private double Salary;

    public Doctor(string Name,int Age,string Gender,int DoctorID,string Specialization,double Salary) : base(Name,Age,Gender)
    {
        this.DoctorID=DoctorID;
        this.Specialization=Specialization;
        this.Salary=Salary;
    }
    public void DiagnosePatient()
    {
        Console.WriteLine("Diagnose by doctor");
    }
    public void PrescribeMedicine()
    {
        Console.WriteLine("Doctor suggest medicine");
    }
    public override DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine("Doctor ID : "+DoctorID+"\n"+"Specialiazation : "+Specialization+"\n"+"Salary : "+Salary);
    }
}