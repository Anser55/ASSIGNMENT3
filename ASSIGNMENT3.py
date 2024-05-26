import numpy as np
#1 Saving, Writing
# Save to a text file
arr1 = np.array([[4, 2, 0], [7, 2, 0]])
np.savetxt('arrayUNO.txt', arr1)
# Save to a CSV file
arr2 = np.array([[17, 38, 8], [6, 1, 9]])
np.savetxt('arrayDOS.csv', arr2)
# Save a random array to a text file
arr_random = np.random.random((3, 3))
np.savetxt('arrayRAND.npy', arr_random)
#2 Loading
# Load from text file
lud2 = np.loadtxt('arrayUNO.txt')
print(f'TEXT FILE\n{lud2}')
# Load from Random Numpy
lud3 = np.loadtxt('arrayRAND.npy')
print(f'RANDOM NUMPY\n{lud3}')
# Load from CSV file
lud = np.genfromtxt('arrayDOS.csv')
print(f'CSV\n{lud}')




