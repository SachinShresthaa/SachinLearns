class Delivery
{
    protected string customerName;
    protected String address;
    public Delivery(String customerName, String address)
    {
        this.customerName=customerName;
        this.address=address;
    }
    public virtual void DeliverOrder()
    {
        Console.WriteLine("Order delivered");
    }
}