# C950 Package Delivery

### NHP2 TASK 1: WGUPS ROUTING PROGRAM
 
The goal of this assessment is to create an algorithm to sort packages. The packages are sorted by comparing the distance between two delivery addresses to make more optimal delivery routes with a combined distance of no more than 140 miles. Multiple packages have additional stipulations such as needing to be delivered before a particular time or needing to be on a particular truck. 

Once the packages have been sorted, the user is presented with a command line interface which allows them to specify a particular time in HHMM format. Once entered, the user can then choose to enter a specific package ID, in which case the program will display just that package’s status at the entered time, or choose to display the status of all packages. The program runs in a loop until manually exited by the user. 

## A: Algorithm Identification
For this program, I chose to use a nearest-neighbor algorithm. The algorithm computes the distance from the location of the truck to each of the remaining packages to be delivered by that truck, and then selects the shortest distance and delivers the corresponding package next. That package is removed, the location of the truck is updated to that package’s address, and the process is repeated with the remaining packages. 

I chose this algorithm because it is easy to implement. The logic behind it is straightforward, it is reasonably efficient, and it yields a solution that, while not being optimal, is good enough to get the delivery route under 140 miles. Each time the program is run, it sorts the packages; it works even when the packages on the trucks are re-arranged or packages are added or taken away, making it self-adjusting. 

## B: Program Overview 

### B2: Programming Environment
For this program, I used PyCharm 2023.1.2 Community Edition running on macOS Ventura 13.3.1 (a). The version of Python used was 3.11. I used Microsoft Excel version 16.73 to create the CSV files used to hold the data, and this paper was written on Microsoft Word version 16.74.  Both Office applications are part of a Microsoft 365 subscription. 
The software was running on a 2020 M1 Mac Mini with 8 GB of RAM and a 250 GB SSD. 

### B3: Space-Time Complexity
The space-time complexity of the major parts of the program are as follows:
•	Reading the three CSV files and creating tables: O(n) time, O(n) space. 
•	Creating the truck objects: O(n) time, O(n) space.
•	Package sorting algorithm: O(n^2) time, O(n) space.
•	Viewing one package detail: O(n) time, O(1) space.
•	Viewing every package’s detail: O(n) time, O(n) space
•	Overall: O(n^2) time, O(n) space. 

### B4: Scalability and Adaptability
The overall program is in O(n^2) time complexity, so it will scale quadratically with the number of packages. Sorting 40 packages requires 1,600 iterations of the sorting loop. If we increase the number of packages to 50, a 25% increase, it will now perform 2,500 iterations, a 56.25% increase. Increasing the number of packages to 80 would be a 100% increase from the original 40, but would require 6,400 iterations, a 300% increase. 
The overall program is in O(n) space complexity, so will scale linearly. A 100% increase in the number of packages would require a 100% increase in the amount of space. 
The current time complexity is not a problem with a small number of packages, but scaling up the number of packages quickly increases the time required. If WGUPS started delivering thousands of packages a day, this could quickly become a problem, and would necessitate the development of a more time-efficient algorithm. 

### B5: Software Efficiency and Maintainability
The software is efficient given the parameters of the assignment. When given a small number of packages to deliver, it uses a nearest-neighbor algorithm to calculate a delivery route that comes in under the 140 miles threshold. 
The software is well-commented and has a logical flow. The trucks and packages are stored as objects, which makes them easy to update. I have tried to reduce redundant code by making functions where appropriate. This makes the code easier to understand, makes updating and maintaining the code easier, and makes it more portable as the code can be re-used in a different program if necessary. 
I have chosen appropriate names for variables, functions and methods. Functions and methods are all well-commented to explain their purpose. This makes is easier for someone else to understand the code’s purpose and for them to maintain it. 
B6: Self-adjusting Data Structures
Hash tables are an efficient way to store data. They have a space complexity of O(n), which means storing n items uses n amount of space. Because each item in the hash table has a key associated with it, it is not necessary to iterate over the whole table to find something, such as how one would search a table for instance. This means it has a time complexity of O(1). This makes it very efficient to add or remove data from a hash table. 
One downside of hash tables is the occurrence of hash collisions. These occur when two items in the table are assigned the same key. In order to retrieve data from a key with a hash collision, one can search that specific index, but this slows access to the data down. Hash tables are also created with a fixed size. This can be a disadvantage because if the chosen size is too small, it can increase the number of hash collisions. If the size is too large, then the table will consume more memory than necessary. Both these scenarios would reduce the efficiency of the program. 

## D: Data Structures
### D1: Data Structure Explanation
I used a hash table to store the data for my program because of its efficiency. The structure of the hash table also lends itself well to storing the sort of data I needed to store. Each of the packages in the assignment has a unique package ID, and this package ID is used to generate a unique hash. Using a unique identifier helps to avoid hash collisions. I created a package object, and stored this using its unique package ID. This allowed me to store a range of information about each package, and I could then write methods for retrieving or updating the package information. 
For instance, my program has a method which returns the package address when passed the package ID. This method is used as part of a function that returns the address number, which is then used as part of a function that calculated the distance between two addresses by using a lookup table. I added time, status, and truck fields to each package to store the delivery time, the package status, and which truck the package is on, respectively. Storing this information in the hash table makes it very easy to access. For instance, when the user enters a time and package ID, I use the time field to set the status by comparing the entered time to the delivered time. The flexibility of the hash table makes using and updating this information easy. 

## I: Algorithm Justification
### I1: Strengths of the Chosen Algorithm
1.	The algorithm is easy to understand and implement. The algorithm has a logical flow that might mirror how someone would deliver packages in real-life; look which address is closest to them, deliver that package, look which address is now closest, etc. The algorithm being straightforward and intuitive to visualize made it easy to write, and it would also make is easy for someone else to understand if they were maintaining the code.  
2.	Despite being sub-optimal, the algorithm produced results that were “good enough” for the given scenario. The chosen algorithm had to create delivery routes that totaled less than 140 miles for all packages. The nearest neighbor algorithm I implemented resulted in delivery routes that totaled 106 miles, 34 miles under the 140-mile threshold. 
### I2: Verification of Algorithm
The algorithm I implemented satisfied the assignment requirements:
•	Total miles driven by all trucks is less than 140 miles. (As implemented: 106 miles)
•	All 40 packages were delivered.
•	Each truck carried a maximum of 16 packages.
•	Trucks traveled at 18 MPH on average.
•	Packages 3, 18, 36, and 38 were on truck 2. 
•	Package 14 was delivered with 15 and 19.
•	Package 16 was delivered with 13 and 19.
•	Package 20 was delivered with 13 and 15. 
•	Packages 6, 25, 28, and 32 did not leave the depot until after 9:05am. 
•	Package 9 was delivered with the corrected address after 10:20am.
•	A user interface was provided for the user to query package details using the time and package ID. 
### I3: Other Possible Algorithms
1.	Brute force algorithm: this algorithm would look at every possible delivery route in order to determine the shortest, most efficient one. While this could result in a shorter distance that the nearest neighbor algorithm I used, implementing it would be complex, and it would be much more computationally complex. With 40 packages to be delivered, there are 40! possible combinations. That’s a very large number!
2.	Dijkstra’s Algorithm: in the context of this assignment, implementing Dijkstra’s Algorithm would set each delivery address as a vertex on a graph. Distances to each other address would be weighted edges, with the closest distances having a lower weight. The algorithm would visit nearby neighbors of each vertex until all vertexes have been visited. Which this might be more efficient than the algorithm I implemented, it is more complex and harder to code. 
J: Different Approach
If I were to complete the project a second time, I would plan my code better before I started. I had to go back as I was coding and add more things to objects implement what I was adding. I believe if I planned it better from the start, it would have been easier to write and not taken as long. 
Also, there are a few pieces of code that I used a few times, so I would like to make them into functions in order to make my code more efficient and increase its maintainability.
## K: Justify the Data Structure Used
### K1: Verification of Data Structure
The hash table used meets all the requirements for the task:
•	No additional libraries were used.
•	Has an insertion function that takes the specified components as inputs.
•	All packages were delivered on time.
•	Additional requirements were met.
•	Total miles driven to deliver all packages was 108 miles, less than the 140-mile threshold. 
•	Package information is accurately updated and displayed. 
### K1A: Efficiency
The hash table has a time efficiency of O(1). As each item has a unique key, calculating the key and retrieving the data takes the same amount of time regardless of how many packages are added. It does not have to iterate over a list of find the data. 
### K1B: Overhead
The hast table has a space efficiency of O(n), so it grows linearly with the number of packages. That is, it takes n space to store n packages.  
### K1C: Implications
Changes to the number of trucks and/or cities would not affect the time and space complexity of the hash table. The only thing that would affect it is increasing the number of packages. As noted above, this would increase the space complexity linearly, but the time complexity would remain constant. 
### K2: Other Data Structures
A dictionary could have been used in this assignment rather than a hash table. A dictionary has a similar structure in that it uses a key paired with data. However, unlike a hash table, it does not use a unique hash to reference each item. This makes a hash table more efficient in storing and retrieving data. 
	A graph could also have been used in this assignment. This could be combined with Dijkstra’s algorithm in order to calculate a more efficient delivery route.  This could be more efficient but would be harder to implement. 
