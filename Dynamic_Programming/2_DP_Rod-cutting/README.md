# Rod cutting problem
```
Description: 
Given a rod of length n and array prices of length n denoting the cost of pieces of the rod of length 1 to n, find the maximum amount 
that can be made if the rod is cut up optimally.
 - quoted from interviewbit.com


# rod-cutting problem using the bottom-up approach:
```

![Example Usage](/Dynamic_Programming/2_DP_Rod-cutting/sample_BU.png?raw=true)

```
# memoization: 

	Initialize all table entries with a special "not computed" flag
	at flagged entry,
	compute, then replace the flag with true value

	Pros: 
	 - Compute the smaller sub problems "on demand"

	Cons:
	 - Overhead from extra initalization with flag
	 - May end up doing many checks of the flag (in recursive calls)
 

# rod-cutting with top-down approach using memoization:
```

![Example Usage](/Dynamic_Programming/2_DP_Rod-cutting/sample_TD.png?raw=true)
