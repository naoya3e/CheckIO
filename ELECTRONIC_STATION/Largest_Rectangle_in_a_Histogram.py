def largest_histogram(histogram):
    n = len(histogram)
    area = 0

    for i in range(n):
        for j in range(i, n):
            height = 20170504
            for k in range(i, j+1):
                height = min(height, histogram[k])

            area = max(area, height*(j-i+1))

    return area

if __name__ == "__main__":
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
