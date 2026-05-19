abstract class Vehicle
{
    public string driverName="";
    public int vehicleNumber;
    public Vehicle(string driverName,int vehicleNumber)
    {
        this.driverName=driverName;
        this.vehicleNumber=vehicleNumber;
    }
    public void ShowVehicleInfo()
    {
        Console.WriteLine("Driver name: "+driverName+"\n"+"Vehicle Number: "+vehicleNumber);
    }
    public abstract double CalculateFare(double distance);
}