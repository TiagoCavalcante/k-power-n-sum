# k-power-n-sum

Finds the formula for the sum of the kth powers of the first n natural numbers for any positive integer k

## How it works?

This generates the augmented matrix for the linear system of the formula assuming that the formula of the sum of k-th powers is a polynomial of degree k + 1.

## How fast is it?

For small values of k this is very fast, but SymPy gets really slow with big values of k, if you care about performance I'd solve the linear system with C++, using the ideas from [this article](https://dspace.cvut.cz/bitstream/handle/10467/95144/F8-BP-2021-Eyvazov-Emil-Emil_Eyvazov_Thesis.pdf).

Just an idea abot the performance:
```sh
$ time python3 main.py 
1^10 + ... + n^10 = n**11/11 + n**10/2 + 5*n**9/6 - n**7 + n**5 - n**3/2 + 5*n/66

real    0m0.392s
user    0m0.351s
sys     0m0.042s

$ time python3 main.py 
1^20 + ... + n^20 = n**21/21 + n**20/2 + 5*n**19/3 - 19*n**17/2 + 1292*n**15/21 - 323*n**13 + 41990*n**11/33 - 223193*n**9/63 + 6460*n**7 - 68723*n**5/10 + 219335*n**3/63 - 174611*n/330

real    0m16.044s
user    0m15.943s
sys     0m0.101s
```
