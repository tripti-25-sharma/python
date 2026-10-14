#include<iostream>
using namespace std;
int main() {
  int nums[5];
  int new_arr;
  for(int i = 0; i < sizeof(nums); i++) {
    if (nums[i] != 0) {
      int new_arr = nums[i];
    }
  }
  int ans = sizeof(nums)-sizeof(new_arr);
  
}