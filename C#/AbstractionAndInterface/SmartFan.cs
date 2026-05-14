using System;

class SmartFan :
    SmartDevice,
    ISwitchable
{
    public SmartFan(string deviceName)

        : base(deviceName)
    {
    }

    public void TurnOn()
    {
        ShowDevice();

        Console.WriteLine(
            "Smart Fan Turned ON"
        );
    }

    public void TurnOff()
    {
        Console.WriteLine(
            "Smart Fan Turned OFF"
        );
    }
}