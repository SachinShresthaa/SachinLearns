class StringsMethods
{
    public static void AllStringMethodHere()
    {
        String text = "Hello, my name is Sachin Shrestha";

        Console.WriteLine("Length:"+ text.Length);

        Console.WriteLine("Upper: " + text.ToUpper());

        Console.WriteLine("Lower: " + text.ToLower());

        Console.WriteLine("Trim: " + text.Trim());

        Console.WriteLine("Contains World: " +
                          text.Contains("Sachin"));

        Console.WriteLine("StartsWith Hello: " +
                          text.Trim().StartsWith("Hello"));

        Console.WriteLine("EndsWith World: " +
                          text.Trim().EndsWith("Shrestha"));

        Console.WriteLine("Replace: " +
                          text.Replace("Sachin", "Angel"));

        Console.WriteLine("Substring: " +
                          text.Substring(7, 26));

        Console.WriteLine("IndexOf Sachin " +
                          text.IndexOf("Sachin"));

        Console.WriteLine("Insert: " +
                          text.Insert(5, " Namaste"));

        Console.WriteLine("Remove: " +
                          text.Remove(5, 16));

        Console.WriteLine("Equals: " +
                          text.Equals("Hello"));

        Console.WriteLine("Compare: " +
                          string.Compare("abc", "abc"));

        string fruits = "Apple,Banana,Mango";

        string[] result = fruits.Split(',');

        foreach(string item in result)
        {
            Console.WriteLine(item);
        }

        string first = "Sachin";
        string last = "Shrestha";

        Console.WriteLine(string.Concat(first, last));

        Console.WriteLine($"Hello {first} {last}");
    }
}