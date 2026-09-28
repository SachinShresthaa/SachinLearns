class CarDelivery : Delivery
{
    int carNumber;
    public CarDelivery(string customerName, string address, int carNumber) : base(customerName, address)
    {
        this.carNumber = carNumber;
    }
    public override void DeliverOrder()
    {
        Console.WriteLine("Customer: " +
                          customerName);

        Console.WriteLine("Address: " +
                          address);

        Console.WriteLine("Car Number: " +
                          carNumber);

        Console.WriteLine("Order delivered by Car");
    }
}