public class Solution {
    public IList<string> FizzBuzz(int n) {
        string[] output = new string[n];

        for (int i = 1; i <= n; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                output[i-1] = "FizzBuzz";
            }
            else if (i % 3 == 0)
            {
                output[i-1] = "Fizz";
            }
            else if (i % 5 == 0)
            {
                output[i-1] = "Buzz";
            }
            else
            {
                output[i-1] = i.ToString();
            }
        }

        return output;
    }
    
    // Time Complexity: O(n)
    // Space Complexity: O(1) excluding the output array
}