using System.Net.Mail;

class MainMethod
{
    static void Main(String[] args)
    {
        // BikeDelivery b1 = new BikeDelivery("Sachin","Manthali","425");
        // CarDelivery c1 = new CarDelivery("Sumit","mahindranagar",400);
        // DroneDelivery d1 = new DroneDelivery("Angel","Mulpani",20);

        // List<Delivery> deliveries = new List<Delivery>();
        // deliveries.Add(b1);
        // deliveries.Add(c1);
        // deliveries.Add(d1);
        // foreach(Delivery Del in deliveries)
        // {
        //     Del.DeliverOrder();
        // }

        List<ZBankAccount> BA = new List<ZBankAccount>();
        BA.Add(new ZSavingAccount("Sumit",10000));
        BA.Add(new ZCurrentAccount("Angel",1000));
        BA.Add(new ZFixedDepositAccount("Prasun",20000));

        foreach(ZBankAccount account in BA)
        {
            account.withdraw(7000);
            account.DisplayBalance();
        }
    }
}