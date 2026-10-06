import numpy as np
arr2=np.array(
[[2, 3, 4], 
[5, 6, 7]]
)
arr2[1, 1]=13
arr2[0, 2]=4
arr2=arr2 +5
arr2=np.delete(arr2,0,axis=0)

print(arr2)
arr3=np.array([
[[1, 2, 3], [4, 5, 6]],
[[7, 8, 9], [10, 11, 12]],
[[13, 14, 15], [16, 17, 18]]
])
print(arr3)
arr3[0,1,1]=17
print(arr3)
arr3=np.delete(arr3,2,axis=0)
print(arr3)
arr3=np.append(arr3,[[[19, 20, 21], [22, 23, 24]]],axis=0)
print(arr3)


