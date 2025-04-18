class Solution
{
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>> &grid)
    {

        int n = grid[0].size();
        vector<int> v;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                v.push_back(grid[i][j]);
            }
        }
        sort(v.begin(), v.end());
        for (auto i : v)
            cout << i << " ";
        int l = n * n;
        int missingNum, duplicateNum;
        if (v[0] != 1)
        {
            missingNum = 1;
        }
        else if (v[l - 1] != l)
        {
            missingNum = l;
        }

        for (int i = 1; i < l; i++)
        {

            if (v[i] - v[i - 1] == 0)
            {
                duplicateNum = v[i];
            }

            if (v[i] - v[i - 1] == 2)
            {
                // missingNum = v[i-1] + 1; // Writing in terms of smaller Num.
                missingNum = v[i] - 1;
            }
        }

        return {duplicateNum, missingNum};
    }
};

//   2 3 3 4 5 6 7 8 9
//   1 2 3 3 4 5 6 7 8
//   1 2 3 4 6 7 8 9 9