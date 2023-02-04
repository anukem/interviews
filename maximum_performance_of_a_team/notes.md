[[Hard]]
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

Example 1:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60

Explanation:
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68

Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72

---
Used this opportunity to try and write the solution in OCaml. Took a couple hours, but here's the answer

```
module PriorityQueue =

struct

type priority = int

type 'a queue = Empty | Node of priority * 'a * 'a queue * 'a queue

let empty = Empty

let rec size = function

Empty -> 0

| Node(prio, elt, left, Empty) -> 1 + size left

| Node(prio, elt, Empty, right) -> 1 + size right

| Node(prio, elt, (Node(lprio, lelt, _, _) as left),

(Node(rprio, relt, _, _) as right)) ->

1 + (size left) + (size right)

let rec insert queue prio elt =

match queue with

Empty -> Node(prio, elt, Empty, Empty)

| Node(p, e, left, right) ->

if prio <= p

then Node(prio, elt, insert right p e, left)

else Node(p, e, insert right prio elt, left)

exception Queue_is_empty

let rec remove_top = function

Empty -> raise Queue_is_empty

| Node(prio, elt, left, Empty) -> left

| Node(prio, elt, Empty, right) -> right

| Node(prio, elt, (Node(lprio, lelt, _, _) as left),

(Node(rprio, relt, _, _) as right)) ->

if lprio <= rprio

then Node(lprio, lelt, remove_top left, right)

else Node(rprio, relt, left, remove_top right)

let extract = function

Empty -> raise Queue_is_empty

| Node(prio, elt, _, _) as queue -> (prio, elt, remove_top queue)

end;;

  

type perf_tracker = {pq: int PriorityQueue.queue; current_sum: int; max_perf: int}

  
  

let get_elt (prio, elt, queue) = elt

let get_max_perf {max_perf} = max_perf

  

let maximum_performance speeds efficiencies k =

let engineers = List.map2 (fun x y -> (x,y)) efficiencies speeds in

let sorted_engineers = List.sort (fun (x, _) (y, _) -> y - x) engineers in

  

let answer = List.fold_left (fun {pq; current_sum; max_perf} (cur_eff, cur_speed) ->

let capacityMet = (PriorityQueue.size pq) > (k - 1) in

if capacityMet then

let poppedHeap = PriorityQueue.remove_top pq in

let newSum = current_sum - (PriorityQueue.extract pq |> get_elt) + cur_speed in

{

pq=(PriorityQueue.insert poppedHeap cur_speed cur_speed);

current_sum=newSum;

max_perf=max max_perf (newSum*cur_eff)

}

else

let updatedSum = current_sum + cur_speed in

{

pq=(PriorityQueue.insert pq cur_speed cur_speed);

current_sum=updatedSum;

max_perf=max max_perf (updatedSum*cur_eff)

})

{pq=PriorityQueue.empty; current_sum=0; max_perf=0} sorted_engineers in

get_max_perf answer

  

let assertIntEquals = fun message x y ->

if x = y

then (String.concat "" ["SUCCESS: "; message])

else (String.concat "" ["FAILURE: "; message; ", expected "; (string_of_int y); ", got "; (string_of_int x)]);;

  
  

print_endline (assertIntEquals "first case" (maximum_performance [2;10;3;1;5;8] [5;4;3;9;7;2] 2) 60);;

print_endline (assertIntEquals "second" (maximum_performance [2;10] [3;4] 2) 40);;

print_endline (assertIntEquals "third" (maximum_performance [2;10;4] [3;4;10] 2) 56);;

print_endline (assertIntEquals "check that size == 3" (

PriorityQueue.size (

PriorityQueue.insert (

PriorityQueue.insert (

PriorityQueue.insert PriorityQueue.empty 1 1)

2 41)

4 12)

) 3);;

  

print_endline (assertIntEquals "check that size == 1" (

PriorityQueue.size (

PriorityQueue.insert PriorityQueue.empty 1 1)

) 1);;

  

print_endline (assertIntEquals "test min at the top" (

PriorityQueue.extract (

PriorityQueue.insert (

PriorityQueue.insert (

PriorityQueue.insert PriorityQueue.empty 3 3)

1 1)

2 2)

|> get_elt ) 1);;
```
