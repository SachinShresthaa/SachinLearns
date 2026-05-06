using System;
class SwitchCase
{
    static void Main (string[] args)
    {
        int day = 3;

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