class MainMethod
{
    static void Main(string[] args)
    {
        // List<ISwitchable> devices =
        //     new List<ISwitchable>();

        // devices.Add(
        //     new SmartLight("Bedroom Light")
        // );

        // devices.Add(
        //     new SmartFan("Hall Fan")
        // );

        // foreach(ISwitchable device in devices)
        // {
        //     device.TurnOn();

        //     Console.WriteLine();
        // }

        List<Vehicle> vehicles = new List<Vehicle>();
        vehicles.Add( new CarRide("Manish",009));
        vehicles.Add( new BikeRide("Bhupen",010));
        vehicles.Add( new PremiumRide("Sumit",011));

        foreach(Vehicle vel in vehicles)
        {
            vel.ShowVehicleInfo();
            Console.WriteLine("Fare: "+vel.CalculateFare(50));
        }

    }
}