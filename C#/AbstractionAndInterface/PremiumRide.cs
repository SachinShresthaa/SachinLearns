
class PremiumRide : Vehicle, IRide
{
    public PremiumRide(string driverName,int vehicleNumber):base(driverName, vehicleNumber)
    {
    }
    public void StartRide()
    {
        Console.WriteLine("Premium ride started");
    
    }
    public void EndRide()
    {
        Console.WriteLine("Premium Ride Ended");
    }
    public override double CalculateFare(double distance)
    {
        return distance*200;
    }
}
