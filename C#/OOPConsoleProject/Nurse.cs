class Nurse : Person
{
    private int WardNumber;
    private string ShiftTiming="";

    public Nurse(string Name,int Age,string Gender,int WardNumber,string ShiftTiming) : base(Name,Age,Gender)
    {
        this.WardNumber=WardNumber;
        this.ShiftTiming=ShiftTiming;
    }
    public void AssistDoctor()
    {
        Console.WriteLine("Assisted");
    }
    public override DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine("Ward Number : "+WardNumber+"\n"+"Shift Timing : "+ShiftTiming);
    }
}