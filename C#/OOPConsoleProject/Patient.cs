class Patient : Person
{
    private int PatientID;
    private string Disease="";
    private int RoomNumber;
    private double BillAmount;

    public Doctor(string Name,int Age,string Gender,int PatientID,string Disease,int RoomNumber, double BillAmount) : base(Name,Age,Gender)
    {
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
    public override DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine("Patient ID : "+PatientID+"\n"+"Disease : "+Disease+"\n"+"Room Number : "+RoomNumber+"\n"+"Bill Amount: "+BillAmount);
    }
}