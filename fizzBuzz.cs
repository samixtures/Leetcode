public class Solution
{
    public IList<string> FizzBuzz(int n)
    {
        string[] output = new string[n];

        for (int i = 1; i <= n; i++)
        {
            String currentString = "";
            bool divisibleBy3 = i % 3 == 0;
            bool divisibleBy5 = i % 5 == 0;


            if (divisibleBy3)
            {
                currentString += "Fizz";
            }
            if (divisibleBy5)
            {
                currentString += "Buzz";
            }
            if (currentString == "")
            {
                currentString = i.ToString();
            }

            output[i - 1] = currentString;
        }

        return output;
    }

    // Time Complexity: O(n)
    // Space Complexity: O(1) excluding the output array
}