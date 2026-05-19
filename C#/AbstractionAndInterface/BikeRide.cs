class BikeRide : Vehicle , IRide
{
    public BikeRide(string driverName,int bikeNumebr):base(driverName, bikeNumebr)
    {
    }
    public void StartRide()
    {
        Console.WriteLine("Bike ride started");
    
    }
    public void EndRide()
    {
        Console.WriteLine("Bike Ride Ended");
    }
    public override double CalculateFare(double distance)
    {
        return distance*50;
    }
}
