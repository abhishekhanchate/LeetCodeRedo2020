class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profits = []
        profit = 0
        queue = 0
        on = 0
        gon = 0
        for i in range(len(customers)):
            if customers[i] < 4 and queue >= 4:
                on = on + 4
                queue = queue + customers[i] - 4
                gon = gon + 1
                profits.append(boardingCost * on - runningCost * gon)
                # print(profits)

            elif customers[i] < 4:
                on = on + customers[i]
                gon = gon + 1
                profits.append(boardingCost * on - runningCost * gon)
                # print(profits)

            else:
                on = on + 4
                queue = queue + customers[i] - 4
                gon = gon + 1
                profits.append(boardingCost * on - runningCost * gon)
                # print(profits)

        while queue > 0:
            on = on + min(4, queue)
            queue = queue - 4
            gon = gon + 1
            profits.append(boardingCost * on - runningCost * gon)
            # print(profits)

        pos = 0
        for i in range(len(profits)):
            if profits[i] >= 0:
                pos = 1

        if pos > 0:
            return profits.index(max(profits)) + 1

        else:
            return -1
