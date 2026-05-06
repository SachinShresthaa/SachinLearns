using System;
class SwitchCase
{
    static void Main (string[] args)
    {
        Console.Write("Enter the day");
        int day = Convert.ToInt32(Console.ReadLine());

switch(day)
{
    case 1:
        Console.WriteLine("Sunday");
        break;

    case 2:
        Console.WriteLine("Monday");
        break;

    case 3:
        Console.WriteLine("Tuesday");
        break;

    default:
        Console.WriteLine("Invalid");
        break;
}
    }
}