public class Solution
{
    public int NumberOfSteps(int num)
    {
        int numberOfSteps = 0;
        while (num > 0)
        {
            if ((num & 1) == 0)
                num = num >> 1;
            else
                num -= 1;

            numberOfSteps += 1;
        }

        return numberOfSteps;
    }
}

// Time Complexity: O(log(n)) since we iterate less than num times?
// Space Complexity: O(1)