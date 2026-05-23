class RoomFullException
    : Exception
{
    public RoomFullException(
        string message)

        : base(message)
    {
    }
}