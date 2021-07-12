# Triangle Data Challenge

The statistical analysis based around triangles of payment figures for previous claims.

The numbers in the input file are the amounts of payments made in respect of claims on a particular block of insurance policies. The claims will be broken into origin years. For example, all claims originally happening in 1996 will go into the
1996 row of the triangle.

## The Problem

Create a program to read in incremental payment data from a comma-separated text file, to
accumulate the data and to output the results to a different comma-separated text file. This process represents the
creation of the cumulative data triangle from the incremental data triangle above.

## Example Input Data
A short input file might contain the following:

Product, Origin Year, Development Year, Incremental Value <br />
Comp, 1992, 1992, 110.0 <br />
Comp, 1992, 1993, 170.0 <br />
Comp, 1993, 1993, 200.0 <br />
Non-Comp, 1990, 1990, 45.2 <br />
Non-Comp, 1990, 1991, 64.8 <br />
Non-Comp, 1990, 1993, 37.0 <br />
Non-Comp, 1991, 1991, 50.0 <br />
Non-Comp, 1991, 1992, 75.0 <br />
Non-Comp, 1991, 1993, 25.0 <br />
Non-Comp, 1992, 1992, 55.0 <br />
Non-Comp, 1992, 1993, 85.0 <br />
Non-Comp, 1993, 1993, 100.0 <br />

This example file contains two triangles – one for a product called ‘Comp’ and one for a product called ‘Non-Comp’. The
first row contains column headings, and the subsequent rows contain the data, so, for example, for accidents occurring
on the Non-Comp product in 1990, 45.2 was paid in 1990, 64.8 was paid in 1991 and 37 was paid in 1993.<br />

The output file corresponding to the above input file would be:<br />
1990, 4<br />
Comp, 0, 0, 0, 0, 0, 0, 0, 110, 280, 200<br />
Non-Comp, 45.2, 110, 110, 147, 50, 125, 150, 55, 140, 100<br />

The first line gives the earliest origin year (i.e. 1990) and the number of development years (in this case ranging from
1990 through to 1993 i.e. 4). <br />
After the first line, there is a line for each triangle. The first field in the line gives the name of the product. The
subsequent fields are the accumulated triangle values.


