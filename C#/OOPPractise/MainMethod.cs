using System;

class MainMethod
{
    static void Main(string[] args)
    {
        // ClassAndObject obj = new ClassAndObject();
        // obj.Display("Sachin");

        // Student s1 = new Student("sachin", 22, "BCA", 99.99);
        // Student s2 = new Student("Angel", 20);
        // s1.DisplayStudentInfo();
        // s2.DisplayStudentInfo();

        // Calculator calc = new Calculator();
        // Console.WriteLine(calc.Add(2, 5));
        // Console.WriteLine(calc.Add(2, 5.6));
        // Console.WriteLine(calc.Add(2, 5, 7));

        // Animal d1 = new Dog();
        // d1.Sound();

        // Animal cat1 = new Cat();
        // cat1.Sound();

        // Car car1 = new Car();
        // car1.Drive();
        // car1.Start();

        IMobile m1 = new IMobile();
        m1.PlayMusic();
        m1.TakePhoto();
    }
}