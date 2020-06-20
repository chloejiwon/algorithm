#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
private:
    vector<int> merged;

public:
    void merge(vector<int> &arr, int left, int right)
    {
        // 이미 정렬된 arr[left~mid], arr[mid+1 ~ right]
        // 두 부분을 merge한다
        int mid = (left + right) / 2;
        int i = left, j = mid + 1, k = 0;
        while (i <= mid && j <= right)
        {
            if (arr[i] < arr[j])
            {
                merged.push_back(arr[i++]);
            }
            else
            {
                merged.push_back(arr[j++]);
            }
        }

        //남은 거 정리
        while (i <= mid)
        {
            merged.push_back(arr[i++]);
        }
        while (j <= right)
        {
            merged.push_back(arr[j++]);
        }
        // 완벽히 merge된 list 로 바꾸기
        vector<int>::iterator iter = merged.begin();
        for (k = left; k <= right && iter != merged.end(); k++, iter++)
        {
            arr[k] = *iter;
        }
        merged.clear();
    }
    void mergeSort(vector<int> &arr, int left, int right)
    {
        if (left < right)
        {
            int mid = (left + right) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, right);
        }
    }
};
int main()
{
    Solution sol;
    vector<int> arr;
    int N;
    int tmp = 0;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &tmp);
        arr.push_back(tmp);
    }
    sol.mergeSort(arr, 0, N - 1);
    // range-based for loop
    /* 
    for (auto iter : arr)
    {
        printf("%d\n", iter);
    }
    */
    for (int i = 0; i < N; i++)
    {
        printf("%d\n", arr[i]);
    }

    return 0;
}