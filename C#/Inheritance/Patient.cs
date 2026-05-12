using System.ComponentModel.Design.Serialization;

class Patient:Person
{
    public String disease="";
    public int roomNumebr;

    public Patient(String name , int age,String disease,int roomNumebr) : base(name,age)
    {
        this.disease=disease;
        this.roomNumebr=roomNumebr;
    }
    public void DisplayPatientInfo()
    {
        Console.WriteLine("Disease: "+disease+"\n"+"Room Number: "+roomNumebr);
    }
}