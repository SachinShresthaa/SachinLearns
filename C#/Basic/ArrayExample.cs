class ArrayExample
{
    public static void ShowArrayOperations()
    {
        int[] numbers = {10, 20, 30, 40, 50};

        int sum = 0;

        foreach(int num in numbers)
        {
            sum += num;
        }

        Console.WriteLine("Sum of Array: " + sum);

        Console.WriteLine();

        Console.WriteLine("Reverse Array:");

        for(int i = numbers.Length - 1; i >= 0; i--)
        {
            Console.WriteLine(numbers[i]);
        }

        Console.WriteLine();

        int search = 30;

        bool found = false;

        foreach(int num in numbers)
        {
            if(num == search)
            {
                found = true;
                break;
            }
        }

        if(found)
        {
            Console.WriteLine(search + " Found in Array");
        }
        else
        {
            Console.WriteLine(search + " Not Found");
        }
    }
}