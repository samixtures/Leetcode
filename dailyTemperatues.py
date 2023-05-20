class Solution:
    def dailyTemperatures(self, sample: List[int]) -> List[int]:
        answer = []

        currentNumber = sample[0]

        for i in range(1, len(sample)):
            newestNumber = sample[i]
            if newestNumber <= currentNumber:
                trailingIndex = i
                counter = 1
                print("NewestNumb", newestNumber)
                print("trailingIndex", trailingIndex)
                while newestNumber <= currentNumber and trailingIndex < len(sample)-1:
                    trailingIndex += 1
                    newestNumber = sample[trailingIndex]
                    counter += 1
                if newestNumber <= currentNumber and trailingIndex >= len(sample)-1:
                    print("runs")
                    counter = 0
                answer.append(counter)
            else:
                answer.append(1)
            currentNumber = sample[i]

        if sample:
            answer.append(0)

        return answer