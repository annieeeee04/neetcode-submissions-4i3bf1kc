class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        const res = [];
        if (nums.length <= 1) return [nums];
        
        let first = nums[0];
        let permutes = this.permute(nums.slice(1));

        for (let p of permutes) {
            for (let i = 0; i <= p.length; i++) {
                let copy = [...p];
                copy.splice(i, 0, first);
                res.push(copy);
            }
        }
        return res;
    }
}
