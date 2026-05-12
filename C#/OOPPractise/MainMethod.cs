using System;
using System.Reflection;
using System.Reflection.Emit;

class MainMethod
{
    static void Main(string[] args)
    {
        // ClassAndObject obj = new ClassAndObject();
        // obj.Display("Sachin");

        // Student s1 = new Student("sachin",22,"BCA",99.99);
        // Student s2 = new Student("Angel", 20);
        // s1.DisplayStudentInfo();
        // s2.DisplayStudentInfo();

        Calculator c1 = new Calculator();
        Console.WriteLine(c1.Add(2,5));
        Console.WriteLine(c1.Add(2,5.6));
        Console.WriteLine(c1.Add(2,5,7));
    }
}