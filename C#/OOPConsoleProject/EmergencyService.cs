class EmergencyService : MedicalService
{
    public override void StartService()
    {
        Console.WriteLine("Emergency Service started");
    
    }
    public override void StopService()
    {
        Console.WriteLine("Emergency Service stopped");
    }
}