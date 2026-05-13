class ZFixedDepositAccount : ZSavingAccount
{
    public ZFixedDepositAccount(string accountHolder, double balance): base(accountHolder,balance)
    {
    }
    public override void withdraw(double amount)
    {
        Console.WriteLine("Withdrawal not allowed before maturity");
    }
}