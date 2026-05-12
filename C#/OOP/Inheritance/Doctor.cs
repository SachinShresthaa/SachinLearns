class Doctor:Person
{
    public string specialization="";
    public int salary;

    public Doctor(string name , int age ,string specialization,int salary):base(name,age)
    {
        this.specialization=specialization;
        this.salary=salary;
    }
    public void DisplayDoctorInfo()
    {
        Console.WriteLine("Specialization: "+specialization+"\n"+"Salary: "+salary);
    }
}