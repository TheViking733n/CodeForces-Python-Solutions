// Programmer: The Viking
// Date: 19.08.2022


import java.util.*;

class sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size of array: ");
        int n = sc.nextInt();
        System.out.print("Enter array: ");
        System.out.flush();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        HashMap<Integer,Integer> freq = new HashMap<Integer,Integer>();
        HashMap<Integer,Integer> ind = new HashMap<Integer,Integer>();
        for (int i = n - 1; i >= 0; i--) {
            ind.put(arr[i], i);
            int count = freq.containsKey(arr[i]) ? freq.get(arr[i]) : 0;
            freq.put(arr[i], count + 1);
        }
        List<ArrayList<Integer>> nums = new ArrayList<>();

        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int v = entry.getKey();
            int f = entry.getValue();
            int i = ind.get(v);
            ArrayList<Integer> temp = new ArrayList<>();
            temp.add(-f);
            temp.add(i);
            temp.add(v);
            nums.add(temp);
        }
        Collections.sort(nums, new Comparator<ArrayList<Integer>>() {
            @Override
            public int compare(ArrayList<Integer> a, ArrayList<Integer> b) {
                if (a.get(0) != b.get(0)) {
                    return a.get(0) - b.get(0);
                } else {
                    return a.get(1) - b.get(1);
                }
            }
        });
        for (ArrayList<Integer> num : nums) {
            System.out.print(num.get(2) + " ");
        }
        System.out.print("\n");
    }
}