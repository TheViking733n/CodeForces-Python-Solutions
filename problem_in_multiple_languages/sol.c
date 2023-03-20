// Programmer: The Viking
// Date: 19.08.2022


#include <stdio.h>
#include <stdlib.h>

struct Node {
    int v;  // value
    int f;  // frequency
    int i;  // index
};
int N;      // No. of unique elements

int cmpfunc(const void* a, const void* b) {
   return ( *(int*)a - *(int*)b );
}

int cmpfunc_node(const void* a, const void* b) {
    struct Node* x = (struct Node*)a;
    struct Node* y = (struct Node*)b;
    int v = y->f - x->f;
    if (v == 0) {
        return x->i - y->i;
    }
    return v;
}

int main() {
    int n;
    printf("Enter size of array: ");
    scanf("%d", &n);
    int* arr = (int*)malloc(n * sizeof(int));
    int* a2 = (int*)malloc(n * sizeof(int));
    printf("Enter array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", arr + i);
        a2[i] = arr[i];
    }
    
    qsort(a2, n, sizeof(int), cmpfunc);
    N = 1;
    int last = a2[0];
    for (int i = 1; i < n; i++) {
        if (a2[i] != last) {
            N++;
            last = a2[i];
        }
    }
    struct Node* nums = (struct Node*)malloc(N * sizeof(struct Node));
    last = a2[0];
    int j = 0;
    nums[j].v = a2[0];
    nums[j].f = 0;

    for (int i = 1; i < n; i++) {
        if (a2[i] != last) {
            nums[++j].v = a2[i];
            nums[j].f = 0;
            last = a2[i];
        }
    }
    for (int j = 0; j < N; j++) {
        for (int i = 0; i < n; i++) {
            if (arr[i] == nums[j].v) {
                nums[j].f++;
                if (nums[j].f == 1)
                    nums[j].i = i;
            }
        }
    }

    qsort(nums, N, sizeof(struct Node), cmpfunc_node);

    for (int i = 0; i < N; i++)
        printf("%d%c", nums[i].v, " \n"[i == N - 1]);
    
    return 0;
}