For this homework, In constructor of Rollinghash and Multidict class I made a 
function call to the append and put method respectly. I used a dictionary with values
of type list to implement Multidict.

11.1-2 
On a certain place of the array, if there used to be a pointer, we put a 1 there, and a 0 otherwise, This will work since there is no satellite data. Looking up takes O(1) since we just need to check if that place is 1. Adding also takes O(1) since we just need to put a 1 there.

11.2-2 
0-nil 1-28,19,10 2-20 3-12 4-nil 5-5,33 6-15 7-nil 8-17

11.2-3 
Insertion becomes slower, all other operation becomes faster

11.3-1 
First compute the hash value for the given key. 
Then for each element in the list compare the string only if the hash value you computed is the same as the hash value for the given key

11.3-4 700 318 936 554 172

11.4-1 
Linear: (31,28,22,17,59,nil,nil,4,15,88,10) 
Quadratic: (17,31,4,15,22,88,59,nil,nil,28,10) 
Double: = (17,59,31,22,nil,nil,15,28,4,88,10)

11.4-2 hash_delete(k) hash_value(k)=x count = 0 while count <= hash_table.length(): if hash_table(x)==k: hash_table.(x) = 'DELETED' break else: x = (x + 1) mod hash_table.length count += 1 hash_insert(k) i = 0 repeat j = h(k,i) if T[j] == nil or T[j] == DELETED: T[j] = k return k else: i = i + 1 until i ==m error "hash table overflow"

17.1-1 No. The bound becomes O(k) now.

Time spent - code - 2 hours, Exercises - 3 hours.
