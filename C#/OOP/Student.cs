class Student
{
    public string name;
    public int rollno;
    public string faculty;
    public double marks;
    public Student(string name, int rollno, string faculty, double marks)
    {
        this.name=name;
        this.rollno=rollno;
        this.faculty=faculty;
        this.marks=marks;
    }

    public Student(string name, int rollno)
    {
    this.name=name;
    this.rollno=rollno;
    faculty="unknown";
    marks=0;    
    }
    public void DisplayStudentInfo()
    {
        Console.WriteLine("Name: "+name);
        Console.WriteLine("Rollno: "+rollno);
        Console.WriteLine("Faculty: "+faculty);
        Console.WriteLine("Marks: "+marks);    
        }
}