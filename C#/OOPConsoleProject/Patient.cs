public class Patient : Person, IHospitalOperations
{
    private int PatientID;
    private string Disease="";
    private int RoomNumber;
    private double BillAmount;

    public Patient(string Name,int Age,string Gender,int PatientID,string Disease,int RoomNumber, double BillAmount) : base(Name,Age,Gender)
    {
        if (Age <= 0)
        {
            throw new Exception("GHOSTTTTT???");
        }
        this.PatientID=PatientID;
        this.Disease=Disease;
        this.RoomNumber=RoomNumber;
        this.BillAmount=BillAmount;
    }
    public void BookAppointment()
    {
        Console.WriteLine("Appointment booked");
    }
    public void ShowBill()
    {
        Console.WriteLine("Bill amount"+ BillAmount);
    }
    public void AdmitPatient()
    {
        Console.WriteLine("Patient admitted");
    }
    public void DischargePatient()
    {
        Console.WriteLine("Patient discharged");
    }
    public void GenerateBill()
    {
        Console.WriteLine("Bill Generated");
    }
    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine("Patient ID : "+PatientID+"\n"+"Disease : "+Disease+"\n"+"Room Number : "+RoomNumber+"\n"+"Bill Amount: "+BillAmount);
    }
}