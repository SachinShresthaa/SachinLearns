public abstract class Person
{
    protected string Name;
    protected int Age;
    protected string Gender;

public Person(string Name, int Age, string Gender)
    {
        this.Age=Age;
        this.Name=Name;
        this.Gender=Gender;
    }
    public virtual void DisplayInfo()
    {
        Console.WriteLine("Name : "+Name+"\n"+"Age : "+Age+"\n"+"Gender : "+Gender+"\n");
    }
}