using System;
using System.Reflection;
using System.Reflection.Emit;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices.Marshalling;

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

        // Calculator c1 = new Calculator();
        // Console.WriteLine(c1.Add(2,5));
        // Console.WriteLine(c1.Add(2,5.6));
        // Console.WriteLine(c1.Add(2,5,7));

        // Animal d1 = new Dog();
        // d1.Sound();
    
        // Animal c1 = new Cat();
        // c1.Sound();

        // Car c1 = new Car();
        // c1.Drive();
        // c1.Start();

        IMobile m1 = new IMobile();
        m1.PlayMusic();
        m1.TakePhoto();
    }
}