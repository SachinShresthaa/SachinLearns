class CollectionExample
{
    public static void ShowCollectionExample(){
        List<String> names = new List<String>();
        names.Add("Sachin");
        names.Add("Angel");
        names.Add("Prasun");
        
        foreach(string name in names)
        {
          Console.WriteLine(name);  
        }

        Dictionary<int,String> Fruits = new Dictionary<int, string>();
        Fruits.Add(1,"Apple");
        Fruits.Add(2,"Banana");
        Fruits.Add(3,"Mango");

        foreach(var fruit in Fruits)
        {
            Console.WriteLine(fruit.Key+":"+fruit.Value);
        }
    }
}