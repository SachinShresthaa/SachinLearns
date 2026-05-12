class Person
{
    public string name="";
    public int age;
    public Person(String name, int age)
    {
        this.name= name;
        this.age=age;
    }
    public void DisplayPersonInfo()
    {
        Console.WriteLine("Name: "+name+"\n"+"Age: "+age);
    }
}