class ZCurrentAccount : ZBankAccount
{
    
    public ZCurrentAccount(string accountHolder, double balance):base(accountHolder,balance){
        
    }
    public override void withdraw(double amount)
    {
        if (balance - amount <= -5000)
        {
            Console.WriteLine("OverDraft");
        }
        else
        {
            balance-=amount;
        }
    }

}