

class CarRide : Vehicle, IRide
{
    public CarRide(string driverName,int bikeNumebr):base(driverName, bikeNumebr)
    {
    }
    public void StartRide()
    {
        Console.WriteLine("Car ride started");
    
    }
    public void EndRide()
    {
        Console.WriteLine("Car Ride Ended");
    }
    public override double CalculateFare(double distance)
    {
        return distance*100;
    }
}
