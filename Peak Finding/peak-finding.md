### Peak Finder
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
> T(n) = T(n/2) + &Theta;(1) , where &Theta;(1) represents the comparisons done on the left hand side and the right hand side as 2 is a constant so &Theta;(1) is used instead <br>
**Base case** when one starts expanding the above equation: 
> T(1) = &Theta;(1) for one element array, the single element is going to be returned as a peak <br>
If the equation is expanded all the way out, then <br>
T(n) = &Theta;(1) + ... + &Theta;(1) <br>
               |___________| <br>
                log<sub>2</sub>n times <br>
        = &Theta;(log<sub>2</sub>n)

