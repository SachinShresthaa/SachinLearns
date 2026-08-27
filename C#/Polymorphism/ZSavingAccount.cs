class ZSavingAccount : ZBankAccount
{
    public ZSavingAccount(string accountHolder,double balance) : base(accountHolder,balance)
    {
    }
    public override void withdraw(double amount)
    {
        if(balance-amount>=1000){
        balance-=amount;        }
        else
        {
            Console.WriteLine("Amount will go less than 1000");
        }
    }
}