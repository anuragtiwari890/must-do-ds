# problem link - https://www.geeksforgeeks.org/dsa/minimum-number-platforms-required-railwaybus-station/

# Minimum Number of Platforms Required for a Railway/Bus Station

# ------------------------------------------------------------------------------------------------
# Problem Statement:
    # Given two arrays arr[] and dep[], that represent the arrival and departure time of i-th train respectively. 
    # Find the minimum number of platforms required so that no train has to wait. 
    # If the departure time of one train is the same as the arrival time of another train, both trains cannot use the same platform at that time.

    # #Note: Time intervals are in the 24-hour format (HHMM), 
    # where the first two characters represent hour (between 00 to 23) and the last two characters represent minutes (this will be <= 59 and >= 0). 
    # Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).

# ------------------------------------------------------------------------------------------------
# Examples:
    # Input: arr[] = [1000, 935, 1100], dep[] = [1200, 1240, 1130]
    # Output: 3
    # Explanation: We need 3 platforms for the arrival of these trains because all three trains have overlapping time.

    # Input: arr[] = [900, 1235, 1100], dep[] = [1000, 1240, 1200]
    # Output: 1
    # Explanation: Only 1 platform is required for all the three trains because the departure time of each train is less then arrival time of next train.

# ------------------------------------------------------------------------------------------------
# approaches:
    # [Naive Approach] Using Two Nested Loops - O(n2) time and O(1) space
        # The idea is to iterate through each train and for that train, 
        # check how many other trains have overlapping timings with it - 
        # where current train's arrival time falls between the other train's arrival and departure times. 
        # We keep track of this count for each train and continuously update our answer with the maximum count found.

    # Time complexity: O(n2)
    # Space complexity: O(1)

    # [Better Approach] Using MinHeap - O(n log(n)) Time and O(n) Space
        # The idea is that each arriving train either reuses a platform freed by a departed train or requires a new one if none are free. 
        # To track this, we sort the trains by arrival time and use a min-heap to store departure times of trains currently on platforms. 
        # Before placing a new train, we remove all trains that have already departed. The heap size then shows how many platforms are in use,
        #  and the maximum size reached during the process is the minimum number of platforms required.

    # Expected Approach: [Expected Approach 1] Using Sorting and Two Pointers - O(n log(n)) Time and O(1) Space
        # The idea is to sort arrivals and departures independently and use two pointers: 
        # i for arrivals and j for departures. 
        # Traverse both arrays. 
        # If the next train arrives before or at the next departure, we need one more platform (arr[i] <= dep[j]). 
        # Otherwise, one train has departed before the next arrival, so we free a platform. Keep updating the maximum number of platforms required.

        # Why Individual Sorting Works?
            # Normally, we might think pairing each arrival with its departure is required. 
                # But here, we only care about when platforms are occupied, not about exact train timings.
            # By sorting arrivals → we always process trains in order of when they come.
            # By sorting departures → we always free platforms in order of when they leave.
            # So, at every step we just compare the next arrival and next departure:

# ------------------------------------------------------------------------------------------------

# solution:
def minPlatform(arr, dep):
    n = len(arr)
    res = 0
    
    arr.sort()
    dep.sort()
    
    j = 0;
    cnt = 0;
    
    # Check for each train
    for i in range(n):
        
        # Decrement count if other 
        # trains have left 
        while j < n and dep[j] < arr[i]:
            cnt -= 1
            j += 1
        
        # one platform for current train 
        cnt += 1
        
        res = max(res, cnt)
    
    return res

if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minPlatform(arr, dep))


    
