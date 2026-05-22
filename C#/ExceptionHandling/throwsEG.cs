class throwsEG
{
    public void throooooo()
    {
        try
        {
            int age = 15;
            if (age < 18){
                throw new Exception("Not eligible for vote");
            }
            Console.WriteLine("Eligible");
        }
        catch(Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
}