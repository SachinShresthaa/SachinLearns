using System;

class basicEH
{
    public void EH()
    {
        try
        {
            int a = 10;
            int b = 0;

            int result = a / b;

            Console.WriteLine(result);
        }

        catch(Exception ex)
        {
            Console.WriteLine(
                "Error: " + ex.Message
            );
        }
    }
}