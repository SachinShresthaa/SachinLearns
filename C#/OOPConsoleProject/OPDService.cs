class OPDService : MedicalService
{
    public override void StartService()
    {
        Console.WriteLine("OPD Service started");
    
    }
    public override void StopService()
    {
        Console.WriteLine("OPD Service stopped");
    }
}