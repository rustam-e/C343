I couldn't get the bfs to work. Not sure why.


22.1-1: compute the out-degree, require O(V+E) time. in-degree, have to go through entire list of vertices, require O(V^2+E) time.

22.1-3: O(V+E).

22.2-1: d π 1 ∞ Ø 2 3 4 3 0 Ø 4 2 4 5 1 3 6 1 3

22.2-4 Each vertex and adjacent vertices so O(v^2)

22.3-2: Tree edges: (q, s), (s, v), (v, w), (q, t), (t, x), (x, z), (t, y), (r, u) Back edges: (w, s), (z, x), (y, q) Forward edges: (q, w) Cross edges: (r, y), (u, y)

22.3-11: outgoing edges point to vertices examined before u and incoming edges are pointed from verticesexamined after u.

22.4-1: m n o p q r s t u v w x y z d 1 21 22 27 2 6 23 3 7 10 11 15 9 12 f 20 26 25 28 5 19 24 4 8 17 14 16 18 13

p -> n -> o -> s -> m -> r -> y -> v -> x -> w -> z -> u -> q -> t

22.5-2: finishing times: q r s t u v w x y z d 1 17 2 8 18 3 4 9 13 10 f 16 20 7 15 19 6 5 12 14 11

Compute the transpose q r s t u v w x y z d 5 1 15 7 3 17 16 11 6 12 f 10 2 20 8 4 18 19 14 9 13

components: {r} -> {u} -> {q, y, t} -> {x, z} -> {s, w, v}

Time spent:
6 hours on programmin 1-2 hours questions.