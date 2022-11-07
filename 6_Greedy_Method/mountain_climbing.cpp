#include <iostream>

using namespace std;
typedef unsigned int uint;


uint calculate_Time(const uint *heights, uint length, uint rest, uint limit, uint burst) {
/*
  Description : greedy algorithm to see time required to climb up the mountain
Arguments : 
  ( const uint ) *heights: An array of the heights of ledges on a cliff (feet)
  ( uint ) length: The amount of ledges on a cliff
  ( uint ) rest: How many seconds you have to rest between bursts
  ( uint ) limit: The amount of time you have to climb the mountain
Returns :
  ( uint ) The amount of time to climb the mountain based on burst.
           will return limit+1 if it is impossible to climb the mountain for a given burst value.
           this indicates that the burst value must increase if we want to climb the mountain.
  */
    uint rests = 0;
    uint reachableHeight = burst;
  
    for (uint i = 0; i < length; i++) {
        uint nextStep = heights[i];
        if (reachableHeight >= nextStep) {
            // next step is reachable without a rest
            continue;
        }
        
        reachableHeight = heights[i-1] + burst;
        if (reachableHeight < heights[i]) {
            // Impossible to reach the next step after a rest
            return (++limit);
        } else {
            rests++;
        }
        
    }

    return (rests*rest + heights[length-1]);
}


uint climbing(const uint *heights, uint length, uint rest, uint limit) {
/*
  Description : Applies binary search to calculate the lowest burst value.
Arguments : 
  ( const uint ) *heights: An array of the heights of ledges on a cliff (feet)
  ( uint ) length: The amount of ledges on a cliff
  ( uint ) rest: How many seconds you have to rest between bursts
  ( uint ) limit: The amount of time you have to climb the mountain
Returns :
  ( uint ) the lowest burst value you can have to climb the mountain before time runs out
  */
    
    uint high = heights[length-1]; // high limit is the last value in heights
    uint low = heights[0]; // just before the lowest value

    while (low < high){
        uint avg = (low + high)/2;
    
        if (calculate_Time(heights,length,rest,limit,avg) <= limit) {
            // there may be a burst value even lower, keep checking.
            high = avg;
        } else  {
            // took too much time, must increase the burst time
            low = avg+1;
        }

    }

    return low;
}


int main(){

    // input
    uint length, rest, limit;
    cin >> length >> rest >> limit;

    uint heights[length];
    for (uint i = 0; i < length; i++) {
        cin >> heights[i];
    }

    // output user input
    cout << '\n' << "Input: " << endl;
    cout << '\t' <<"Length: " << length << ", Rest: " << rest;
    cout << ", Limit: " << limit << endl;
    cout << '\t'<< "Heights: " << "[ ";
    for (const auto &value: heights) {
    std::cout << value << ' ';
    }
    cout << ']' << endl;

    // output the minimum burst value needed to climb the mountain
    cout << "Output:" << endl;
    cout << '\t' << "Minimum Burst: " << climbing(heights,length,rest,limit) << '\n' << endl;


    return 0;
}