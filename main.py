##################################################
## Developer Problem
##################################################

## Author: Subhash Reddy K
## Version: 3.0
## Email: abhisubhash@gmail.com
## Status: 2 Pending To-Do tasks

##################################################
## This script is written to solve a Developer Problem
## as part of interview and is not intended for anyone
## other than the interviewer to read or modify
##################################################


import pandas as pd
import chainladder as cl
import numpy as np


# To-Do
# 1. Read from a .txt file instead of a .csv

def read_data():
    read_data_df = pd.read_csv('input.csv', sep=",")

    # preprocess_data(read_data_df)

    no_of_years = len(read_data_df['Development Year'].unique())
    print(no_of_years)

    origin_year = read_data_df['Development Year'].unique()[0]
    print(origin_year)

    product_name = read_data_df['Product'].unique()[0]
    print(product_name)

    print(read_data_df)
    to_triangular_data(read_data_df, origin_year, no_of_years, product_name)


# To-Do
# 2. Handle error in unexpected format
# 3. Separate DataFrame based on unique product names

# def preprocess_data(read_input_data):
#     read_input_data.columns = read_input_data.columns.str.lower()
#     del read_input_data['product']


def to_triangular_data(read_input_data, origin_year, no_of_years, product_name):
    # Convert the Pandas Dataframe to Triangular Data Format
    triangle_data = cl.Triangle(read_input_data, origin='Origin Year', development='Development Year',
                                columns='Incremental Value',
                                cumulative=False)
    print(triangle_data)
    triangle_data_cum = triangle_data.incr_to_cum()
    print(triangle_data_cum)

    # Find the format of Triangle Data and replace NaN values with 0
    print('Data structure of triangle_data_cum:', type(triangle_data_cum.values))
    triangle_data_cum = np.nan_to_num(triangle_data_cum.values)
    print(triangle_data_cum)

    # Remove redundant dimensions in Numpy Array
    triangle_data_cum_2d = triangle_data_cum.squeeze()
    print(triangle_data_cum_2d)
    save_to_txt_file(triangle_data_cum_2d, origin_year, no_of_years, product_name)


def save_to_txt_file(squeezed_np_array, origin_year, no_of_years, product_name):
    np.savetxt('output.txt', squeezed_np_array, delimiter=',', newline=',', fmt='%d')

    with open('output.txt') as text_file:
        contents = text_file.read()
        print(contents)

    final_txt = open('output.txt', 'w')
    final_txt.write(
        str(origin_year) + ',' + str(no_of_years) + '\n' + product_name + ',' + contents.rstrip(contents[-1]))
    final_txt.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_data()
