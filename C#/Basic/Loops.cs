using System;

class AllLoops
{
    static void Main(string[] args)
    {
        // FOR LOOP
        Console.WriteLine("FOR LOOP");

        for(int i = 1; i <= 5; i++)
        {
            Console.WriteLine(i);
        }

        Console.WriteLine();


        // WHILE LOOP
        Console.WriteLine("WHILE LOOP");

        int j = 1;

        while(j <= 5)
        {
            Console.WriteLine(j);
            j++;
        }

        Console.WriteLine();


        // DO-WHILE LOOP
        Console.WriteLine("DO-WHILE LOOP");

        int k = 1;

        do
        {
            Console.WriteLine(k);
            k++;
        }
        while(k <= 5);

        Console.WriteLine();


        // FOREACH LOOP
        Console.WriteLine("FOREACH LOOP");

        string[] fruits = {"Apple", "Banana", "Mango"};

        foreach(string fruit in fruits)
        {
            Console.WriteLine(fruit);
        }
    }
}