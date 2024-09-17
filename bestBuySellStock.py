def maxProfit(prices):
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            diff = prices[r] - prices[l]
            maxP = max(diff, maxP)
        else:
            l = r
        r = r + 1

    return maxP

def main():
    print(maxProfit([10,1,5,6,7,1]))


if __name__ == "__main__":
    main()