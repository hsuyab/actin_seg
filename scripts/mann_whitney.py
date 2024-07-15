# mann_whitney_u_test.py

from scipy.stats import mannwhitneyu, norm
import numpy as np
from tabulate import tabulate

def mann_whitney_u_test(data1, data2, alpha=0.05, name_data1='Data 1', name_data2='Data 2'):
    """
    Perform Mann-Whitney U test on two datasets and print the results.

    Args:
        data1 (array-like): First dataset
        data2 (array-like): Second dataset
        alpha (float): Significance level (default: 0.05)
        name_data1 (str): Name of the first dataset (default: 'Data 1')
        name_data2 (str): Name of the second dataset (default: 'Data 2')

    Returns:
        None (prints results to console)
    """
    # Perform Mann-Whitney U test
    stat, p = mannwhitneyu(data1, data2)
    
    # Calculate sample sizes
    n1, n2 = len(data1), len(data2)
    
    # Calculate effect size (rank biserial correlation)
    effect_size = stat / (n1 * n2)

    # Calculate confidence interval
    z_critical = norm.ppf(1 - alpha / 2)  # Two-tailed test
    se = (n1 * n2 * (n1 + n2 + 1) / 12) ** 0.5
    ci_low = (stat - z_critical * se) / (n1 * n2)
    ci_high = (stat + z_critical * se) / (n1 * n2)

    # Calculate statistical power
    z_score = abs(norm.ppf(p / 2))
    power = 1 - norm.cdf(z_critical - z_score)

    # Calculate descriptive statistics
    median1, median2 = np.median(data1), np.median(data2)
    mean1, mean2 = np.mean(data1), np.mean(data2)
    std1, std2 = np.std(data1), np.std(data2)

    # Print test results
    print(f"Doing Mann Whitney U Test for {name_data1} and {name_data2}")
    if p > alpha:
        print("The two datasets are not significantly different (fail to reject H0)")
    else:
        print("The two datasets are significantly different (reject H0)")

    test_results = [
        ["p-value", p],
        ["Effect size (rank biserial correlation)", effect_size],
        ["Confidence interval for the difference in medians", f"[{ci_low}, {ci_high}]"],
        ["Statistical power", power]
    ]
    print("\nTest Results:")
    print(tabulate(test_results, headers=["Metric", "Value"], tablefmt="grid"))

    descriptive_stats = [
        ["Dataset", "Median", "Mean", "Standard Deviation", "Sample Size"],
        [name_data1, median1, mean1, std1, n1],
        [name_data2, median2, mean2, std2, n2]
    ]
    print("\nDescriptive Statistics:")
    print(tabulate(descriptive_stats, headers="firstrow", tablefmt="grid"))

# Example usage
if __name__ == "__main__":
    # Generate some example data
    np.random.seed(42)
    data1 = np.random.normal(loc=0, scale=1, size=100)
    data2 = np.random.normal(loc=0.5, scale=1, size=100)

    # Perform Mann-Whitney U test
    mann_whitney_u_test(data1, data2, name_data1="Control Group", name_data2="Treatment Group")
