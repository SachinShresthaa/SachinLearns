using System;
using System.Collections.Generic;

class MainMethod
{
    static void Main(string[] args)
    {
        List<ISwitchable> devices =
            new List<ISwitchable>();

        devices.Add(
            new SmartLight("Bedroom Light")
        );

        devices.Add(
            new SmartFan("Hall Fan")
        );

        foreach(ISwitchable device in devices)
        {
            device.TurnOn();

            Console.WriteLine();
        }
    }
}