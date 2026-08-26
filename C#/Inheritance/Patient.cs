class Patient : Person
{
    public String disease = "";
    public int roomNumber;

    public Patient(String name, int age, String disease, int roomNumber) : base(name, age)
    {
        this.disease = disease;
        this.roomNumber = roomNumber;
    }
    public void DisplayPatientInfo()
    {
        Console.WriteLine("Disease: " + disease + "\n" + "Room Number: " + roomNumber);
    }
}