#include <stdio.h>
#include <stdlib.h>

int uniques = 1;

// int f(void* a, void* b)
// {
//     int *ptr_a = a, *ptr_b = b;
//     return ptr_a[0] < ptr_b[0] ? -1 : ptr_a[0] > ptr_b[0];
// }

int cmpfunc(const void* a, const void* b) {
   return ( *(int*)a - *(int*)b );
}

int cmpfunc2d(const void* a, const void* b) {
    printf("%d %d %d %d\n", *(int*)a, *(int*)b, *(((int*)a) + uniques), *(((int*)b) + uniques));
    int val = ( *(((int*)a) + uniques) - *(((int*)b) + uniques));
    if (val > 0) {
        int temp = *(((int*)a) + uniques);
        *(((int*)a) + uniques) = *(((int*)b) + uniques);
        *(((int*)b) + uniques) = temp;
    }
    return val;
}

int main() {
    int n;
    printf("Enter size of array: ");
    scanf("%d", &n);
    int* arr = (int*)malloc(n * sizeof(int));
    printf("Enter array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(int), cmpfunc);

    int last = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] != last) {
            uniques++;
            last = arr[i];
        }
    }
    printf("Uniques: %d\n", uniques);
    int* nums = (int*)malloc(2 * uniques * sizeof(int));
    int i = 0, j = uniques;
    nums[i] = arr[0];
    nums[j] = 1;
    for (int k = 1; k < n; k++) {
        if (arr[k] == arr[k - 1]) {
            nums[j]++;
        } else {
            nums[++i] = arr[k];
            nums[++j] = 1;
        }
    }
    for (int k = 0; k < uniques; k++) {
        printf("%d ", nums[k]);
    }
    printf("\n");
    for (int k = uniques; k < 2 * uniques; k++) {
        printf("%d ", nums[k]);
    }
    printf("\n\n");


    // qsort(nums, uniques, sizeof(int), cmpfunc2d);

    int swapped;
    for (int i = 0; i < uniques; i++) {
        swapped = 1;
    }



    for (int k = 0; k < uniques; k++) {
        printf("%d ", nums[k]);
    }
    printf("\n");
    for (int k = uniques; k < 2 * uniques; k++) {
        printf("%d ", nums[k]);
    }
    printf("\n");










    // qsort(nums, sizeof nums / sizeof *nums, sizeof *nums, f);
}