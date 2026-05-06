using System;
using System.Net;
class TypeConversion
{
    static void Main (string[] args)
    {
        Console.Write("enter number");
        string number = Console.ReadLine();
        int n = Convert.ToInt32(number);
        Console.WriteLine("The conversion vaule is:"+n);
    }
}