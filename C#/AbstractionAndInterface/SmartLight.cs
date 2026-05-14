using System;

class SmartLight :
    SmartDevice,
    ISwitchable
{
    public SmartLight(string deviceName)

        : base(deviceName)
    {
    }

    public void TurnOn()
    {
        ShowDevice();

        Console.WriteLine(
            "Smart Light Turned ON"
        );
    }

    public void TurnOff()
    {
        Console.WriteLine(
            "Smart Light Turned OFF"
        );
    }
}