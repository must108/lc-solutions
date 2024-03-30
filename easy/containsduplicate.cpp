#include <iostream>

class Solution {
public:
    int partition(vector<int> & arr, int left, int right) {
        int temp;
        int pivot = left + (right - left) / 2;

        temp = arr[pivot];
        arr[pivot] = arr[left];
        arr[left] = temp;

        pivot = left;
        left += 1;

        while(left <= right) {
            while(left <= right && arr[left] <= arr[pivot]) left += 1;
            while(right >= left && arr[right] > arr[pivot]) right -= 1;

            if(left < right) {
                temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }

        temp = arr[pivot];
        arr[pivot] = arr[right];
        arr[right] = temp;

        return right;
    }

    void quickSort(vector<int> & arr, int low, int high) {
        if(low < high) {
            int k = partition(arr, low, high);

            quickSort(arr, low, k - 1);
            quickSort(arr, k + 1, high);
        }
    }

    bool containsDuplicate(vector<int>& nums) {
        int n = nums.size();
        quickSort(nums, 0, n - 1);

        for(int i = 0; i < n - 1; i++) {
            if(nums[i] == nums[i + 1]) {
                return true;
            }
        }

        return false;
    }
};