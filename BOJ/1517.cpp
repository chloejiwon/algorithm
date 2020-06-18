// merge sort
#include <stdio.h>
#define MAX_ARR 500001
int sorted[MAX_ARR];
long long ans = 0;
// merge two sorted array [left ~ mid ] & array [mid ~ right]
void merge(int *list, int left, int mid, int right)
{
    int i, j, k, l;
    i = left;
    j = mid + 1;
    k = left;

    while (i <= mid && j <= right)
    {
        if (list[i] <= list[j])
        {
            sorted[k++] = list[i++];
        }
        else
        {
            ans += (mid - i + 1);
            sorted[k++] = list[j++];
        }
    }
    while (i <= mid)
    {
        sorted[k++] = list[i++];
    }
    while (j <= right)
    {
        sorted[k++] = list[j++];
    }
    for (l = left; l <= right; l++)
    {
        list[l] = sorted[l];
    }
}
void mergesort(int *arr, int left, int right)
{
    if (left < right)
    {
        int mid = (left + right) / 2;
        mergesort(arr, left, mid);
        mergesort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
int main()
{
    int N;
    int a[500001] = {
        0,
    };
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
        scanf("%d", &a[i]);
    ans = 0;
    mergesort(a, 0, N - 1);
    printf("%lld\n", ans);
}