|   |   |   |   |
|:-:|:-:|:-:|:-:|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |### Peak Finder
#### One dimensional version

| a | b | c | d | e | f | g | h | i |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
1|2|3|4|5|6|7|8|9

a-i are numbers. Position 2 is a **peak** if and only if b &ge; a and b &ge; c. <br>
In case of edges, Position 9 is a **peak** iff i &ge; h.

##### Find a peak if it exists
#### Straightforward Algorithm
- Start from left

|  |  |  |  |  |  |  |  |  |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
1|2||||n/2||n-1|n

The numbers are increasing as you start from the left, the peak is somewhere in the middle and then things start decreasing. In this case, n/2 might be peak. <br>
For finding this peak, you may have to look at n/2 elements <br>
Worst case complexity would be &Theta;(n) as you may have to look at all n elements and that would be the case where you started from the left and you had to go all the way to the right. <br>
&Theta;(n) means for the order of n i.e. it gives both the lower bound and the upper bound. while O(n) is just upper bound.<br>
The **Asymptotic Complexity** of this algorithm is **linear**.<br>
To lower the asymptotic complexity, use **Divide and Conquer Algorithm** and recursively break up this one dimensional array into smaller arrays.

#### Divide and Conquer Algorithm
|  |  |  |  |  |  |  |  |  |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
1|2||n/2-1|n/2|n/2+1|||n-1|n|
- Look at n/2 position, we're gonna look to the left and then to the right and that is done in sequence.
- If a[n/2] &lt; a[n/2-1] then only look at left half i.e 1...n/2-1 to look for a peak.
- Else If a[n/2] &lt; a[n/2+1] then only look at right half i.e n/2+1...n to look for a peak.
- else n/2 position is a peak <br>
If T(n) is the work this algorithm does on input of size n, then <br>
T(n) = T(n/2) + &Theta;(1) , where &Theta;(1) represents the comparisons done on the left hand side and the right hand side as 2 is a constant so &Theta;(1) is used instead <br>
**Base case** when one starts expanding the above equation: <br>
T(1) = &Theta;(1) for one element array, the single element is going to be returned as a peak <br>
If the equation is expanded all the way out, then <br>
T(n) = &Theta;(1) + ... + &Theta;(1) <br>
               |___________| <br>
                log<sub>2</sub>n times <br>
        = &Theta;(log<sub>2</sub>n)
### 2D Version 
|   |  c |   |   |
|:-:|:-:|:-:|:-:|
| b  |  a |  d |   | 
|   |  e |   |   |
|   |   |   |   |

m columns and n rows <br>
a is a 2D peak iff a &ge; b, a &ge; d, a &ge; c, a &ge; e <br>
#### Greedy Ascent Algorithm
It essentially picks a direction and tries to follow that direction in order to find a peak.

|   |   | 10  |   |
|:-:|:-:|:-:|:-:|
| 14  |  13 |  12 |   | 
| 15  |  9 | 11  |  17 |
| 16  | 17  | 19  | 20  |

Here if you're starting with 12, you're gonna go look to left and if it's greater than, you're gonna follow that direction and if it's less you're gonna go in the other direction. In this case you'll go 12, 13, 14, 15, 16, 17, 19, **20...the peak** <br>

&Theta;(nm) Complexity <br>
&Theta;(n<sup>2</sup>) if m = n <br>

|   |   |   |
|:-:|:-:|:-:|
|   |   |   | i
|   |   |   |
|   |j=m/2|  |

- Pick middle column j = m/2
- Find a 1D-peak at (i,j)
- Use (i,j) as a start to find a 1D-peak on row i
^ ***Incorrect Algorithm*** <br>
**Problem** : 2D peak may not exist on row i <br>
For the above example if you start from 10 then 12 is the peak since 12 &ge; 10 and 12 &ge; 11. and for that row 14 will be the 1D peak but **14 is not a 2D peak** <br>
**Attempt #2** <br>
- Pick middle column j=m/2
- Find global max on column j at (i,j)
- Compare (i,j-1), (i,j), (i,j+1)--meaning once you find the maximum in the row look to the left and the right and compare
- Pick left columns if (i,j-1) &gt; (i,j), and similarly for the right
- If (i,j) &ge; (i,j-1), (i,j+1) => (i,j) is a 2D peak
- Solve the new problem with half the number of columns
- **Base case** when you have a single column, find the global maximum and you're done <br> i.e T(n,1) = &Theta;(n)
##### Complexity
T(n,m) = T(n,m/2) + &Theta;(n), meaning n is the number of rows and m is the number of columns, in one case you'll be breaking things down into half the number of columns which is m over 2 and in order to find the global maximum you'll be doing &Theta;(n) work <br>
T(n,1) = &Theta;(n) <br>
T(n,m) = &Theta;(n) + ... + &Theta;(n) <br>
          |___________|<br> 
                log<sub>2</sub>m times <br>
        = &Theta;(log<sub>2</sub>m)

