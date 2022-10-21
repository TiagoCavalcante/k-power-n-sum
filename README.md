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

real    0m0.403s
user    0m0.351s
sys     0m0.052s

$ time python3 main.py 
1^200 + ... + n^200 = n**201/201 + n**200/2 + 50*n**199/3 - ...

real    0m24.700s
user    0m24.545s
sys     0m0.154s
```
