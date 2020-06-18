// 수 정렬하기
#include <stdio.h>
void insertion(int N, int *arr)
{
    int key = 0;
    for (int i = 1; i < N; i++)
    {
        key = arr[i];
        int j = i - 1;
        for (; j >= 0; j--)
        {
            if (arr[j] <= key)
            {
                break;
            }
            else
            {
                arr[j + 1] = arr[j];
            }
        }
        arr[j + 1] = key;
    }
}
int main()
{
    int N, arr[1001];
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }
    insertion(N, arr);
    for (int i = 0; i < N; i++)
    {
        printf("%d\n", arr[i]);
    }
    return 0;
}