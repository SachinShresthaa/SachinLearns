using System;

abstract class SmartDevice
{
    protected string deviceName;

    public SmartDevice(string deviceName)
    {
        this.deviceName = deviceName;
    }

    public void ShowDevice()
    {
        Console.WriteLine(
            "Device Name: " +
            deviceName
        );
    }
}