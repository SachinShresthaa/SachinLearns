using System;

class Program
{
    static void Main()
    {
        double a, b, c;
        double sum, mul, div;

        // Input
        Console.Write("Enter first number: ");
        a = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter second number: ");
        b = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter third number: ");
        c = Convert.ToDouble(Console.ReadLine());

        // Calculations
        sum = a + b + c;
        mul = a * b * c;

        // Check for division by zero
        if (b != 0 && c != 0)
        {
            div = (a / b) / c;
        }
        else
        {
            Console.WriteLine("Division not possible (division by zero).");
            div = 0;
        }

        // Output
        Console.WriteLine("\nSum = " + sum);
        Console.WriteLine("Multiplication = " + mul);
        Console.WriteLine("Division = " + div);

        Console.ReadLine();
    }
}