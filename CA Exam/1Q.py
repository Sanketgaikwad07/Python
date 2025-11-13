
#List and loop

nums = list(map(int, input("Enter integers separated by space: ").split()))


largest = float('-inf')
second_largest = float('-inf')
smallest = float('inf')
second_smallest = float('inf')

even_sum = 0
even_count = 0


for num in nums:
  
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

   
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

  
    if num % 2 == 0:
        even_sum += num
        even_count += 1


print("\nSecond Largest:", "Not found" if second_largest == float('-inf') else second_largest)
print("Second Smallest:", "Not found" if second_smallest == float('inf') else second_smallest)

if even_count > 0:
    avg_even = even_sum / even_count
    print("Average of Even Numbers:", avg_even)
else:
    print("No even numbers found.")
