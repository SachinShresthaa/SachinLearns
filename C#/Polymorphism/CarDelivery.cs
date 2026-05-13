class CarDelivery : Delivery
{
    int CarNumber;
    public CarDelivery(string customerName , string address, int CarNumber):base(customerName ,address)
    {
        this.CarNumber=CarNumber;
    }
 public override void DeliverOrder()
    {
        Console.WriteLine("Customer: " +
                          customerName);

        Console.WriteLine("Address: " +
                          address);

        Console.WriteLine("Bike Number: " +
                          CarNumber);

        Console.WriteLine("Order delivered by Car");
    }
}