public class mainMethod
{
    static void Main(string[] args)
    {
        List<Person> p = new List<Person>();
        bool running = true;

        while (running)
        {
            Console.WriteLine("\n===== Hospital Management System =====");
            Console.WriteLine("1. Add Doctor");
            Console.WriteLine("2. Add Patient");
            Console.WriteLine("3. Show All Records");
            Console.WriteLine("4. Exit");
            Console.Write("Enter Choice: ");
            int Choice = Convert.ToInt32(Console.ReadLine());

            switch (Choice)
            {
                case 1:
                    Console.Write("Enter Doctor Name: ");
                    string dname =Console.ReadLine();

                    Console.Write( "Enter Doctor Age: ");
                    int dage =Convert.ToInt32(Console.ReadLine());

                    Console.Write("Enter Gender: ");
                    string dgender =Console.ReadLine();

                    Console.Write("Enter Doctor ID: ");
                    int did =Convert.ToInt32(Console.ReadLine());

                    Console.Write("Enter Specialization: ");
                    string specialization =Console.ReadLine();

                    Console.Write("Enter Salary: ");
                    double salary =Convert.ToDouble(Console.ReadLine());
                    
                    Doctor d1 =new Doctor(dname,dage,dgender,did,specialization,salary);
                    p.Add(d1);
                    Console.WriteLine("Doctor Added Successfully");
                    break;
                case 2:
                    try{
                        Console.Write("Enter Patient Name: " );
                        string pname =Console.ReadLine();

                        Console.Write("Enter Patient Age: ");
                        int page = Convert.ToInt32(Console.ReadLine());

                        Console.Write("Enter Gender: ");
                        string pgender =Console.ReadLine();

                        Console.Write("Enter Patient ID: " );
                        int pid =Convert.ToInt32(Console.ReadLine());

                        Console.Write("Enter Disease: ");
                        string disease =Console.ReadLine();

                        Console.Write("Enter Room Number: ");
                        int room =Convert.ToInt32(Console.ReadLine());

                        Console.Write("Enter Bill Amount: ");
                        double bill =Convert.ToDouble(Console.ReadLine());

                        Patient p1 =new Patient(pname,page,pgender,pid,disease,room,bill);
                        p.Add(p1);
                        Console.WriteLine("Patient Added Successfully");
                    }
                    catch(Exception ex){
                        Console.WriteLine(ex.Message);
                    }
                    finally
                    {
                        Console.WriteLine("Patient Process Finished");
                    }
                    break;
                case 3:
                    foreach(Person pe in p){
                        Console.WriteLine();
                        pe.DisplayInfo();
                    }
                    break;
                case 4:
                    running = false;
                    Console.WriteLine("System Closed");
                    break;
                default:
                    Console.WriteLine("Invalid Choice");
                    break;
            }
        }
    }
}