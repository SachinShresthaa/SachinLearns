using System;

class InvalidPinException
    : Exception
{
    public InvalidPinException(
        string message)

        : base(message)
    {
    }
}