using System;

class ATM
{
    private int correctPin = 1234;

    private double balance = 5000;

    public void StartATM()
    {
        try
        {
            Console.Write("Enter PIN: ");

            int pin =
                Convert.ToInt32(
                    Console.ReadLine()
                );

            if(pin != correctPin)
            {
                throw new
                    InvalidPinException(
                        "Invalid ATM PIN"
                    );
            }

            Console.Write(
                "Enter Withdrawal Amount: "
            );

            double amount =
                Convert.ToDouble(
                    Console.ReadLine()
                );

            if(amount > balance)
            {
                throw new
                    InsufficientBalanceException(
                        "Insufficient Balance"
                    );
            }

            balance -= amount;

            Console.WriteLine(
                "Withdrawal Successful"
            );

            Console.WriteLine(
                "Remaining Balance: " +
                balance
            );
        }

        catch(InvalidPinException ex)
        {
            Console.WriteLine(
                ex.Message
            );
        }

        catch(
            InsufficientBalanceException ex)
        {
            Console.WriteLine(
                ex.Message
            );
        }

        catch(FormatException)
        {
            Console.WriteLine(
                "Invalid Input"
            );
        }

        catch(Exception ex)
        {
            Console.WriteLine(
                "Error: " + ex.Message
            );
        }

        finally
        {
            Console.WriteLine(
                "ATM Session Closed"
            );
        }
    }
}