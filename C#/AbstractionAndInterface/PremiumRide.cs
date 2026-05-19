
class PremiumRide : Vehicle, IRide
{
    public PremiumRide(string driverName,int bikeNumebr):base(driverName, bikeNumebr)
    {
    }
    public void StartRide()
    {
        Console.WriteLine("Premium ride started");
    
    }
    public void EndRide()
    {
        Console.WriteLine("Preminum Ride Ended");
    }
    public override double CalculateFare(double distance)
    {
        return distance*200;
    }
}
