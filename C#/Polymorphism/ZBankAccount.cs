using System.Diagnostics.Contracts;

class ZBankAccount
{
    protected string accountHolder;
    protected double balance;
    

    // protected double deposit;
    public ZBankAccount(string accountHolder, double balance)
    {
        this.accountHolder=accountHolder;
        this.balance=balance;
    }
    public virtual void Deposit(double amount)
    {
        balance+=amount;
        Console.WriteLine("Deposited successfull");
    }
    public virtual void withdraw(double amount)
    {
        balance-=amount;
        Console.WriteLine("Withdrawl sucessfull");
    }
    public  void DisplayBalance()
    {
        Console.WriteLine("Account Holder name: "+accountHolder);
        Console.WriteLine("Balance"+balance);
    }

}