class DroneDelivery : Delivery
{
    int droneNumber;
    public DroneDelivery(string customerName , string address, int droneNumber):base(customerName ,address)
    {
        this.droneNumber=droneNumber;
    }
    public override void DeliverOrder()
    {
        Console.WriteLine("Customer: " +
                          customerName);

        Console.WriteLine("Address: " +
                          address);

        Console.WriteLine("Drone Number: " +
                          droneNumber);

        Console.WriteLine("Order delivered by drone");
    }
}