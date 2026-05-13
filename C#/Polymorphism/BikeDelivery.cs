using System.Diagnostics;

class BikeDelivery : Delivery
{
    private string bikeNumber;
    public BikeDelivery(string customerName , string address, string bikeNumber):base(customerName ,address)
    {
        this.bikeNumber=bikeNumber;
    }
 public override void DeliverOrder()
    {
        Console.WriteLine("Customer: " +
                          customerName);

        Console.WriteLine("Address: " +
                          address);

        Console.WriteLine("Bike Number: " +
                          bikeNumber);
                          
        Console.WriteLine("Order delivered by Bike");
    }
}