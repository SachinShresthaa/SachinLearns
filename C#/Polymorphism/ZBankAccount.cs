class ZBankAccount
{
    protected string accountHolder;
    protected double balance;

    public ZBankAccount(string accountHolder, double balance)
    {
        this.accountHolder = accountHolder;
        this.balance = balance;
    }
    public virtual void Deposit(double amount)
    {
        balance += amount;
        Console.WriteLine("Deposited successfully");
    }
    public virtual void withdraw(double amount)
    {
        balance -= amount;
        Console.WriteLine("Withdrawal successful");
    }
    public void DisplayBalance()
    {
        Console.WriteLine("Account Holder name: " + accountHolder);
        Console.WriteLine("Balance: " + balance);
    }

}