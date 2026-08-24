class Calculator
{
    public static void StartCalculator()
    {
        Console.Write("Enter First Number: ");
        Double num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter The Opertor(+,-,*,/): ");
        String Opertor = Console.ReadLine();

        Console.Write("Enter Second Number: ");
        Double num2 = Convert.ToDouble(Console.ReadLine());

        double result = 0;

        switch (Opertor)
        {
            case ("+"):
                result = num1 + num2;
                break;
            
            case("-"):
                result = num1 - num2;
                break;

            case("*"):
                result = num1 * num2;
                break;

            case ("/"):
             if (num2!=0){
                result = num1/num2;
                
                }
                else
                {
                    Console.WriteLine("Cannot divide by 0");
                }break;

            default:
            Console.WriteLine("Invalid Operator");
                return;
        }
        Console.WriteLine("the result is:"+ result);
    }
}