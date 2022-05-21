Dimitri lives in a city which can be represented as an undirected tree with edge weights. Where each vertex corresponds to a building, and each edge corresponds to a road. Each building has a height hi and each road has a distance di.

Dimitri loves paragliding. If he is standing on top of building i, then he can paraglide to building j as long as hi−hj≥d(i,j), where d(i,j) is the distance between building i and building j along the edges of the graph. Buildings i and j
do not need to be adjacent in the graph.

We call a trip a sequence of vertices v1,v2,…,vk
, where for all 1≤i<k, then hvi−hvi+1≥d(vi,vi+1). That is a trip is a sequence of paraglides one after the other. Dimitri gives each trip a numerical value hv1−hvk

. He is now wondering, amoung all trips what is the highest numerical value, can you solve this problem for him?
Input

Each test contains multiple test cases. The first line contains an integer t
(1≤t≤3⋅105) - the number of test cases. The description of the t

test cases follow.

The first line of each test case contains an integer n
(1≤n≤3⋅105)

- the number of buildings.

The second line of each test case contains n
integers h1,…,hn (1≤hi≤109), where hi is the height of the i

-th building.

Next follow n−1
lines, each containing three integers u,v,w (1≤u,v≤n,1≤w≤109), meaning there is an undirected road between building u and v of distance w

.

Edges given will always form a tree.

It is guaranteed that the sum of n
over all test cases does not exceed 3⋅105

.
Output

For each test case, output the highest numerical value of a trip.
