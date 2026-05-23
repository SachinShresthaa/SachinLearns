class EmergencyService : MedicalService
{
    public override void StartService()
    {
        Console.WriteLine("Service started");
    
    }
    public override void StopService()
    {
        Console.WriteLine("Service stopped");
    }
}