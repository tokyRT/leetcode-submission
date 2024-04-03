/**
 * @param {number[]} nums
 * @return {number}
 */
var mostFrequentEven = function (nums) {
    // if(nums.length==1) return nums[0]
    let count = {}
    nums.forEach(num => {
        if (num % 2 == 0) {
            if (num in count) {
                count[num] += 1
            } else {
                count[num] = 1
            }
        }
    })
    let res = nums[0]
    let resCount = 0
    for (const [key, value] of Object.entries(count)) {
        let k=parseInt(key)
        if (value > resCount) {
            resCount = value
            res = k
        } else if (resCount == value && k < res) {
            res = k
        }
    }
    console.log(count)
    return Object.keys(count).length>0 ? res : -1
};